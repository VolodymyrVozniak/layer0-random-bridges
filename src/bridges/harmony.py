import time

import eth_abi.packed
from web3 import Web3
from loguru import logger

from .utils import search_setting_data, transaction_verification
from .settings import SETTING_HARMONYBRIDGE_LIST


def harmony_bridge(name, private_key, from_chain, amount, max_gas, max_value):   
    log_name = f'HARMONY BRIDGE {from_chain} to HARMONY'
    to_chain = 'HARMONY'

    from_data = search_setting_data(chain=from_chain, list=SETTING_HARMONYBRIDGE_LIST)
    if len(from_data) == 0:
        logger.error(f'{name} | {log_name} | Error while finding information about from_chain')
        return
    else:
        from_data = from_data[0]

    ZROADDRESS        = '0x0000000000000000000000000000000000000000'
    DSTCHAIN          = 116 # Harmony
    RPC_FROM          = from_data['RPC']
    BRIDGE            = from_data['BRIDGE']
    BRIDGE_ABI        = from_data['BRIDGE_ABI']
    TOKEN_FROM        = from_data['USDT']
    TOKEN_ABI_FROM    = from_data['USDT_ABI']

    # Connect and check
    w3_from = Web3(Web3.HTTPProvider(RPC_FROM, request_kwargs={"timeout": 120}))
    if w3_from.is_connected() == True:
        account = w3_from.eth.account.from_key(private_key)
        address = account.address
        logger.success(f'{name} | {address} | {log_name} | Connected to {from_chain}')
    else:
        logger.error(f'{name} | {log_name} | Failed connection to {from_chain}')
        return
    
    # Check for tokens
    try:
        contractTOKEN_from = w3_from.eth.contract(address=w3_from.to_checksum_address(TOKEN_FROM), abi=TOKEN_ABI_FROM)
        
        token_symbol_from     = contractTOKEN_from.functions.symbol().call()
        token_decimals_from   = contractTOKEN_from.functions.decimals().call()
        balance_of_token_from = contractTOKEN_from.functions.balanceOf(address).call()
        human_balance         = balance_of_token_from/ 10 ** token_decimals_from

        if amount == 'ALL':
            amountIn = balance_of_token_from
            amount = human_balance
        else:
            amountIn = int(amount * 10 ** token_decimals_from)
        if balance_of_token_from >= amountIn:
            logger.info(f'{name} | {address} | {log_name} | {token_symbol_from} = {human_balance}, there are enough tokens | {from_chain}')
        else:
            logger.info(f'{name} | {address} | {log_name} | {token_symbol_from} = {human_balance} there are not enough tokens | {from_chain}')
            logger.error(f'{name} | {address} | {log_name} | {token_symbol_from} = {human_balance} there are not enough tokens | {from_chain}')
            return
    except Exception as Ex:
        logger.error(f'{name} | {address} | {log_name} | Error on checking the balance | {from_chain} \n {str(Ex)}')
        return
    
    logger.info(f'{name} | {address} | {log_name} | BRIDGE {amount} from {from_chain} to {to_chain}')

    # Approve
    try:
        nonce = w3_from.eth.get_transaction_count(address)
        while True:
            gas = contractTOKEN_from.functions.approve(
                w3_from.to_checksum_address(BRIDGE),
                amountIn
                ).estimate_gas({'from': address, 'nonce': nonce, })
            gas = gas * 1.2
            if from_chain == 'BSC' and 'ankr' in RPC_FROM:
                gas_price = 1500000000
            else:
                gas_price = w3_from.eth.gas_price
            txCost = gas * gas_price
            txCostInEther = w3_from.from_wei(txCost, "ether").real
            if txCostInEther < max_gas:
                logger.info(f'{name} | {address} | {log_name} | Gas cost on approve {txCostInEther}, {from_chain}')
                break
            else:
                logger.warning(f'{name} | {address} | {log_name} | Gas cost on approve {txCostInEther}, {from_chain}, > max_gas')
                time.sleep(30)
                
        transaction = contractTOKEN_from.functions.approve(
                w3_from.to_checksum_address(BRIDGE),
                amountIn
                ).build_transaction(
                    {
                    'from': address,
                    'value': 0,
                    'gas': int(gas),
                    'gasPrice': int(gas_price),
                    'nonce': nonce})
        signed_transaction = account.sign_transaction(transaction)
        transaction_hash = w3_from.eth.send_raw_transaction(signed_transaction.rawTransaction)
        logger.success(f'{name} | {address} | {log_name} | Sign Approve {transaction_hash.hex()}')
        status = transaction_verification(name, transaction_hash, w3_from, from_chain, log_name=log_name, text=f'Approve {amount} | {from_chain}', logger=logger)
        if status == False:
            logger.error(f'{name} | {address} | {log_name} | Error Approve {amount} | {from_chain}')
            return
    except Exception as Ex:
        if "insufficient funds for gas * price + value" in str(Ex):
            logger.error(f'{name} | {address} | {log_name} | Insufficient funds for Approve {amount} | {from_chain} \n {str(Ex)}')
            return
        logger.error(f'{name} | {address} | {log_name} | Error Approve {amount} | {from_chain} \n {str(Ex)}')
        return
    
    time.sleep(10)

    # BRIDGE to Harmony
    try: 
        contractBRIDGE = w3_from.eth.contract(address=w3_from.to_checksum_address(BRIDGE), abi=BRIDGE_ABI)
        nonce = w3_from.eth.get_transaction_count(address)
        while True:
            _adapterParams = eth_abi.packed.encode_packed(["uint16", "uint256"],
                                                  [1, 500000])
            values = contractBRIDGE.functions.estimateSendFee(  DSTCHAIN,
                                                                address,
                                                                amountIn,
                                                                False,
                                                                _adapterParams,
                                                                ).call()
            value = values[0]
            human_value = w3_from.from_wei(value, "ether").real
            if human_value < max_value:
                logger.info(f'{name} | {address} | {log_name} | Value cost on bridge {human_value}, {from_chain}')
            else:
                logger.warning(f'{name} | {address} | {log_name} | Value cost on bridge {human_value}, {from_chain}, > max_value')
                time.sleep(30)
                continue

            gas = contractBRIDGE.functions.sendFrom(
                address,
                DSTCHAIN,
                address,
                amountIn,
                address,
                ZROADDRESS,
                _adapterParams,
                ).estimate_gas({'from': address, 'value':value, 'nonce': nonce,})
            gas = gas * 1.2
            if from_chain == 'BSC' and 'ankr' in RPC_FROM:
                gas_price = 1500000000
            else:
                gas_price = w3_from.eth.gas_price
            txCost = gas * gas_price
            txCostInEther = w3_from.from_wei(txCost, "ether").real
            if txCostInEther < max_gas:
                logger.info(f'{name} | {address} | {log_name} | Gas cost on BRIDGE {txCostInEther}, {from_chain}')
                break
            else:
                logger.warning(f'{name} | {address} | {log_name} | Gas cost on BRIDGE {txCostInEther}, {from_chain}, > max_gas')
                time.sleep(30)
                continue

        transaction = contractBRIDGE.functions.sendFrom(
            address,
            DSTCHAIN,
            address,
            amountIn,
            address,
            ZROADDRESS,
            _adapterParams,                       
            ).build_transaction({
                'from': address,
                'value': value,
                'gas': int(gas),
                'gasPrice': int(gas_price),
                'nonce': nonce})
        signed_transaction = account.sign_transaction(transaction)
        transaction_hash = w3_from.eth.send_raw_transaction(signed_transaction.rawTransaction)
        logger.success(f'{name} | {address} | {log_name} | Sign {transaction_hash.hex()}')
        status = transaction_verification(name, transaction_hash, w3_from, from_chain, log_name=log_name, text=f'Amount {amount} | {from_chain}',  logger=logger)
        if status == False:
            logger.error(f'{name} | {address} | {log_name} | Error amount {amount} | {from_chain}')
            return
        return True
    except Exception as Ex:
        if "insufficient funds for gas * price + value" in str(Ex):
            logger.error(f'{name} | {address} | {log_name} | Insufficient funds amount {amount} | {from_chain} \n {str(Ex)}')
            return
        logger.error(f'{name} | {address} | {log_name} | Error amount {amount} | {from_chain} \n {str(Ex)}')
        return
