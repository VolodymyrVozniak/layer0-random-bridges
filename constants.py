# Possible choices: Aptos, Testnet, Harmony, Bitcoin, Stargate, Merkly
MODULES = ["Aptos", "Testnet", "Bitcoin", "Merkly"]

SLEEP_FROM = 1000
SLEEP_TO   = 2000

RETRY = 10

RANDOM_WALLETS = True
CHOOSE_RANDOM = False
KEEP_DONE_WALLETS = True

PROCESS_ALL = False
N_WALLETS = 5  # Ignore if PROCESS_ALL is True

WALLETS_PATH = "data/wallets.txt"
DONE_WALLETS_PATH = "data/done_wallets.txt"
APTOS_WALLETS_PATH = "data/aptos_wallets.txt"


"""TRADER JOE"""

TRADER_JOE_AMOUNT_FROM = 0.02   # AVAX
TRADER_JOE_AMOUNT_TO   = 0.05   # AVAX
TRADER_JOE_MAX_GAS     = 0.017  # AVAX
TRADER_JOE_MAX_BTC     = 0.1    # BTC


"""APTOS"""

APTOS_AMOUNT_FROM = 0.11  # USDT
APTOS_AMOUNT_TO   = 0.23  # USDT

# Possible choices: Polygon, Arbitrum, BSC
APTOS_SOURCE_CHAINS = ["Polygon"]

APTOS_MAX_GAS = {
    "Polygon": 0.1,       # MATIC
    "Arbitrum": 0.00023,  # ETH
    "BSC": 0.0014         # BNB
}

APTOS_MAX_VALUE = {
    "Polygon": 1.5,       # MATIC
    "Arbitrum": 0.0007,   # ETH
    "BSC": 0.0046         # BNB
}


"""TESTNET"""

TESTNET_AMOUNT_FROM = 0.00008  # ETH
TESTNET_AMOUNT_TO   = 0.00017  # ETH

# Possible choices: Arbitrum, Optimism
TESTNET_SOURCE_CHAINS = ["Arbitrum"]

TESTNET_MAX_GAS = {
    "Arbitrum": 0.0006,  # ETH
    "Optimism": 0.0006   # ETH
}

TESTNET_MAX_VALUE = {
    "Arbitrum": 0.0002,   # ETH
    "Optimism": 0.0002    # ETH
}


"""HARMONY"""

HARMONY_AMOUNT_FROM = 0.11  # USDT
HARMONY_AMOUNT_TO   = 0.23  # USDT

# Possible choices: BSC
HARMONY_SOURCE_CHAINS = ["BSC"]

HARMONY_MAX_GAS = {
    "BSC": 0.0014  # BNB
}

HARMONY_MAX_VALUE = {
    "BSC": 0.0046  # BNB
}


"""BITCOIN"""

BITCOIN_BRIDGE_ALL  = True

# If BITCOIN_BRIDGE_ALL is False, use these values
BITCOIN_AMOUNT_FROM = 0.00001
BITCOIN_AMOUNT_TO   = 0.00002

# Possible choices: Avalanche, Polygon
BITCOIN_SOURCE_CHAINS = ["Avalanche"]

BITCOIN_MAX_GAS = {
    "Avalanche": 0.017,  # AVAX
    "Polygon": 0.1       # MATIC
}

BITCOIN_MAX_VALUE = {
    "Avalanche": 0.08,   # AVAX
    "Polygon": 1.5,      # MATIC
}


"""STARGATE"""

STARGATE_AMOUNT_FROM = 1.3  # USDT or USDC
STARGATE_AMOUNT_TO   = 1.7  # USDT or USDC

# Possible choices: BSC, Arbitrum, Optimism, Polygon, Avalanche, Fantom
STARGATE_FROM_CHAINS = ["Polygon"]
STARGATE_TO_CHAINS   = ["BSC"]

# Possible choices:
# BSC:       USDT
# Arbitrum:  USDT
# Optimism:  USDC
# Polygon:   USDT; USDC
# Avalanche: USDT; USDC
# Fantom:    USDC
STARGATE_FROM_TOKENS = ["USDT"]
STARGATE_TO_TOKENS   = ["USDT"]

STARGATE_MAX_GAS = {
    "BSC": 0.0014,       # BNB
    "Arbitrum": 0.0002,  # ETH
    "Optimism": 0.0002,  # ETH
    "Polygon": 0.1,      # MATIC
    "Avalanche": 0.017,  # AVAX
    "Fantom": 0.25       # FTM
}

STARGATE_MAX_VALUE = {
    "BSC": 0.0046,       # BNB
    "Arbitrum": 0.0006,  # ETH
    "Optimism": 0.0006,  # ETH
    "Polygon": 1.5,      # MATIC
    "Avalanche": 0.08,   # AVAX
    "Fantom": 4          # FTM
}

STARGATE_SLIPPAGE = 0.5  # %


"""MERKLY"""

# Possible choices: optimism, bsc, arbitrum, polygon, zksync, avalanche,
#                   gnosis, fantom, nova, core, celo, moonbeam, moonriver
MERKLY_FROM_CHAINS = ["polygon", "avalanche", "bsc", "fantom", "gnosis", "zksync"]

# Possible choices: avalanche, polygon, ethereum, bsc, arbitrum, optimism,
#                   fantom, aptos, harmony, celo, moonbeam, fuse, gnosis,
#                   klaytn, metis, core, polygon_zkevm, canto, zksync,
#                   moonriver, tenet, nova, kava, meter
MERKLY_TO_CHAINS = {
    "polygon": ["celo", "gnosis", "harmony", "kava", "core", "moonbeam", "moonriver", "nova", "fuse"],
    "avalanche": ["celo", "gnosis", "harmony", "kava", "core", "moonbeam", "moonriver", "nova", "fuse", "klaytn"],
    "bsc": ["celo", "gnosis", "harmony", "kava", "core", "moonbeam", "moonriver", "nova", "fuse", "klaytn"],
    "fantom": ["celo", "gnosis", "harmony", "kava", "moonbeam", "moonriver", "nova"],
    "gnosis": ["celo", "fuse", "klaytn"],
    "zksync": ["nova"]
}

# Amount of native token for each chain [from, to]
MERKLY_AMOUNTS = {
    "celo": [0.04, 0.05],
    "gnosis": [0.01, 0.02],
    "harmony": [1, 2],
    "kava": [0.015, 0.03],
    "core": [0.015, 0.03],
    "moonbeam": [0.5, 1],
    "moonriver": [0.0023, 0.0046],
    "nova": [0.000006, 0.000012],
    "fuse": [0.04, 0.05],
    "klaytn": [0.04, 0.05]
}
