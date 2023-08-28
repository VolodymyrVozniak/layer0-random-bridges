from loguru import logger
from web3 import Web3
from eth_abi import encode

from .utils import get_web3, add_gas_price, sign_tx, add_gas_limit_layerzero, check_status_tx, intToDecimal
from .settings import DATA, ABI_MERKLY_REFUEL, MERKLY_CONTRACTS, LAYERZERO_CHAINS_ID


def get_adapterParams(gaslimit: int, amount: int):
    return Web3.to_hex(encode(["uint16", "uint64", "uint256"], [2, gaslimit, amount])[30:])


def merkly_refuel(name, privatekey, from_chain, to_chain, amount):
    try:
        web3        = get_web3(from_chain)
        account     = web3.eth.account.from_key(privatekey)
        wallet      = account.address

        log_name = f'MERKLY REFUEL {from_chain} to {to_chain}'
        logger.info(f'{name} | {wallet} | {log_name}')

        contract = web3.eth.contract(address=Web3.to_checksum_address(MERKLY_CONTRACTS[from_chain]), abi=ABI_MERKLY_REFUEL)

        value = intToDecimal(amount, 18)
        adapterParams = get_adapterParams(250000, value) + wallet[2:].lower()
        send_value = contract.functions.estimateGasBridgeFee(LAYERZERO_CHAINS_ID[to_chain], False, adapterParams).call()

        contract_txn = contract.functions.bridgeGas(
                LAYERZERO_CHAINS_ID[to_chain],
                '0x0000000000000000000000000000000000000000', # _zroPaymentAddress
                adapterParams
            ).build_transaction(
            {
                "from": wallet,
                "value": send_value[0],
                "nonce": web3.eth.get_transaction_count(wallet),
                'gasPrice': 0,
                'gas': 0,
            }
        )

        if amount > 0:

            if from_chain == 'bsc':
                contract_txn['gasPrice'] = 1000000000
            else:
                contract_txn = add_gas_price(web3, contract_txn)

            contract_txn = add_gas_limit_layerzero(web3, contract_txn)

            tx_hash = sign_tx(web3, contract_txn, privatekey)
            tx_link = f'{DATA[from_chain]["scan"]}/{tx_hash}'

            status = check_status_tx(from_chain, tx_hash)
            if status == 1:
                logger.success(f'{log_name} | {tx_link}')
                return True

            else:
                logger.error(f'{log_name} | tx is failed | {tx_link}')
                return

        else:
            logger.error(f"{log_name} : can't refuel : balance = {amount}")
            return

    except Exception as error:
        logger.error(f'{log_name} | {error}')
        return
