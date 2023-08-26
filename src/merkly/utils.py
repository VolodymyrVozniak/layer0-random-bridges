import random
import time

from web3 import Web3
from loguru import logger

from .settings import ERC20_ABI, DATA, MAX_TIME_CHECK_TX_STATUS


def get_web3(chain):
    rpc = DATA[chain]['rpc']
    return Web3(Web3.HTTPProvider(rpc))


def add_gas_price(web3, contract_txn):
    gas_price = web3.eth.gas_price
    contract_txn['gasPrice'] = int(gas_price * random.uniform(1.01, 1.02))
    return contract_txn


def sign_tx(web3, contract_txn, privatekey):
    signed_tx = web3.eth.account.sign_transaction(contract_txn, privatekey)
    raw_tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = web3.to_hex(raw_tx_hash)
    return tx_hash


def check_data_token(chain, token_address):
    try:
        web3 = Web3(Web3.HTTPProvider(DATA[chain]['rpc']))
        token_contract  = web3.eth.contract(address=Web3.to_checksum_address(token_address), abi=ERC20_ABI)
        decimals        = token_contract.functions.decimals().call()
        symbol          = token_contract.functions.symbol().call()
        return token_contract, decimals, symbol
    except Exception as error:
        logger.error(error)


def decimalToInt(qty, decimal):
    return qty/ int("".join((["1"]+ ["0"]*decimal)))


def intToDecimal(qty, decimal):
    return int(qty * int("".join(["1"] + ["0"]*decimal)))


def add_gas_limit_layerzero(web3, contract_txn):
    pluser = [1.05, 1.07]
    gasLimit = web3.eth.estimate_gas(contract_txn)
    contract_txn['gas'] = int(gasLimit * random.uniform(pluser[0], pluser[1]))
    return contract_txn


def check_status_tx(chain, tx_hash):

    logger.info(f'{chain} : checking tx_status : {tx_hash}')

    start_time_stamp = int(time.time())

    while True:
        try:

            rpc_chain   = DATA[chain]['rpc']
            web3        = Web3(Web3.HTTPProvider(rpc_chain))
            status_     = web3.eth.get_transaction_receipt(tx_hash)
            status      = status_["status"]

            if status in [0, 1]:
                return status

        except Exception as error:
            # logger.info(f'error, try again : {error}')
            time_stamp = int(time.time())
            if time_stamp-start_time_stamp > MAX_TIME_CHECK_TX_STATUS:
                logger.info(f'did not recieve tx_status for {MAX_TIME_CHECK_TX_STATUS} sec, think that tx is success')
                return 1
            time.sleep(1)
