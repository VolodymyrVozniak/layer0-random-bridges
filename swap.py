"""Swap AVAX to BTC.b or BTC.b to AVAX on TraderJoe"""

import random

from src.swap import trade_avax_to_btc, trade_btc_to_avax
from src.utils import sleeping
from .constants import SLEEP_FROM, SLEEP_TO, RANDOM_WALLETS, WALLETS_PATH, \
    TRADER_JOE_AMOUNT_FROM, TRADER_JOE_AMOUNT_TO, TRADER_JOE_MAX_GAS, TRADER_JOE_MAX_BTC


with open(WALLETS_PATH, "r") as f:
    WALLETS = [row.strip() for row in f]

if RANDOM_WALLETS:
    random.shuffle(WALLETS)


if __name__ == "__main__":
    response = int(input('''
Module:
1. Swap AVAX to BTC.b
2. Swap BTC.b to AVAX

Choose module: '''))

    for i, wallet in enumerate(WALLETS):
        if response == 1:
            trade_avax_to_btc(
                name=str(i),
                private_key=wallet,
                value=random.uniform(TRADER_JOE_AMOUNT_FROM, TRADER_JOE_AMOUNT_TO),
                max_gas=TRADER_JOE_MAX_GAS
            )
        elif response == 2:
            trade_btc_to_avax(
                name=str(i),
                private_key=wallet,
                max_btc=TRADER_JOE_MAX_BTC,
                max_gas=TRADER_JOE_MAX_GAS
            )
        else:
            raise NotImplementedError

        sleeping(SLEEP_FROM, SLEEP_TO)
