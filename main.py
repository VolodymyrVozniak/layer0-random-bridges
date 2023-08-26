"""
Use one of the following options at random for multiple wallets:
    * Aptos Bridge (USDT Polygon | BSC | Arbitrum -> USDT Aptos);
    * Testnet Bridge (ETH Arbitrum | Optimism -> GoerliETH Goerli);
    * Harmony Bridge (USDT BSC -> USDT Harmony);
    * Bitcoin Bridge (BTC.b Avalanche <-> BTC.b Polygon);
    * Merkly Refuel.

All settings can be found in constants.py
"""

import random

from loguru import logger

from src.bridges import aptos_bridge, harmony_bridge, testnet_bridge, bitcoin_bridge
from src.merkly import merkly_refuel
from src.utils import sleeping
from .constants import *


with open(WALLETS_PATH, "r") as f:
    WALLETS = [row.strip() for row in f]

if "Aptos" in MODULES:
    with open(APTOS_WALLETS_PATH, "r") as f:
        APTOS_WALLETS = [row.strip() for row in f]
    APTOS_WALLETS_DICT  = dict(zip(WALLETS, APTOS_WALLETS))

if RANDOM_WALLETS:
    WALLETS = random.shuffle(WALLETS)


def run(choice, **kwargs):
    if choice == "Aptos":
        from_chain = random.choice(APTOS_SOURCE_CHAINS)
        return aptos_bridge(
            name=kwargs["name"],
            private_key=kwargs["wallet"],
            from_chain=from_chain,
            wallet=APTOS_WALLETS_DICT[kwargs["wallet"]],
            amount=random.uniform(APTOS_AMOUNT_FROM, APTOS_AMOUNT_TO),
            max_gas=APTOS_MAX_GAS[from_chain],
            max_value=APTOS_MAX_VALUE[from_chain]
        )
    
    elif choice == "Testnet":
        from_chain = random.choice(TESTNET_SOURCE_CHAINS)
        return testnet_bridge(
            name=kwargs["name"],
            private_key=kwargs["wallet"],
            from_chain=from_chain,
            max_bridge=random.uniform(TESTNET_AMOUNT_FROM, TESTNET_AMOUNT_TO),
            max_gas=TESTNET_MAX_GAS[from_chain],
            max_value=TESTNET_MAX_VALUE[from_chain]
        )
    
    elif choice == "Harmony":
        from_chain = random.choice(HARMONY_SOURCE_CHAINS)
        return harmony_bridge(
            name=kwargs["name"],
            private_key=kwargs["wallet"],
            from_chain=from_chain,
            amount=random.uniform(HARMONY_AMOUNT_FROM, HARMONY_AMOUNT_TO),
            max_gas=HARMONY_MAX_GAS[from_chain],
            max_value=HARMONY_MAX_VALUE[from_chain]
        )
    
    elif choice == "Bitcoin":
        from_chain = random.choice(BITCOIN_SOURCE_CHAINS)

        if BITCOIN_BRIDGE_ALL:
            max_bridge = "ALL"
        else:
            max_bridge = random.uniform(BITCOIN_AMOUNT_FROM, BITCOIN_AMOUNT_TO)

        return bitcoin_bridge(
            name=kwargs["name"],
            private_key=kwargs["wallet"],
            from_chain=from_chain,
            to_chain=random.choice(list(set(BITCOIN_SOURCE_CHAINS) - set(from_chain))),
            max_bridge=max_bridge,
            max_gas=BITCOIN_MAX_GAS[from_chain],
            max_value=BITCOIN_MAX_VALUE[from_chain]
        )

    elif choice == "Merkly":
        from_chain = random.choice(MERKLY_FROM_CHAINS)
        to_chain = random.choice(MERKLY_TO_CHAINS[from_chain])
        amounts = MERKLY_AMOUNTS[to_chain]
        return merkly_refuel(
            privatekey=kwargs["wallet"],
            from_chain=from_chain,
            to_chain=to_chain,
            amount=random.uniform(amounts[0], amounts[1])
        )
    
    else:
        raise NotImplementedError


if __name__ == "__main__":
    for i, wallet in enumerate(WALLETS):
        retry = 0

        while retry < RETRY:
            logger.info(f"Running {retry + 1} attempt...")

            status = run(
                choice=random.choice(MODULES),
                name=str(i),
                wallet=wallet
            )

            if status:
                logger.success("Find successful transaction!")
                break
            else:
                sleeping(10, 10)
                retry += 1

        if retry == RETRY:
            logger.error("CANNOT find successful transaction!")

        sleeping(SLEEP_FROM, SLEEP_TO)