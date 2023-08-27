# Overview

This repo allows you to use one of the following options at random for multiple wallets:
* **Aptos Bridge** (`USDT Polygon | BSC | Arbitrum -> USDT Aptos`);
* **Testnet Bridge** (`ETH Arbitrum | Optimism -> GoerliETH Goerli`);
* **Harmony Bridge** (`USDT BSC -> USDT Harmony`);
* **Bitcoin Bridge** (`BTC.b Avalanche <-> BTC.b Polygon`);
* **Stargate Bridge**;
* **Merkly Refuel**.

# Instructions

1. Make sure to have python, pip and git installed.

2. Clone this repo:
```sh
git clone https://github.com/VolodymyrVozniak/layer0-random-bridges.git
```

3. Go to a directory:
```sh
cd layer0-random-bridges
```

4. Add your private keys to `data/wallets.txt` (paste private keys, each from the new line, press Ctrl+O, Enter and Ctrl+X):
```sh
nano data/wallets.txt
```

5. Add your Aptos addresses to `data/aptos_wallets.txt` (paste public addresses, each from the new line, press Ctrl+O, Enter and Ctrl+X):
```sh
nano data/aptos_wallets.txt
```

6. Create virtual environment (can skip this step):
```sh
python -m venv env
```

7. Activate virtual environment (must run every time you connect to a server):
```sh
source env/bin/activate
```

8. Install python requirements (install only once):
```sh
pip install -r requirements.txt
```

9. Run the script to swap AVAX to BTC.b or BTC.b to AVAX on Trader Joe:
```sh
python swap.py
```

10. Run the script to use random bridge for multiple wallets:
```sh
python main.py
```

11. You can modify the following parameters in `constants.py`:

* **General**
    * `MODULES`: Modules to use. Possible choices: `Aptos`, `Testnet`, `Harmony`, `Bitcoin`, `Merkly`;
    * `SLEEP_FROM`: The lowest value to sleep between wallets in seconds;
    * `SLEEP_TO`: The highest value to sleep between wallets in seconds;
    * `RETRY`: Number of retries for one wallet;
    * `RANDOM_WALLETS`: Rather to shuffle wallets;
    * `WALLETS_PATH`: Path for file with private keys (each private key from new line);
    * `APTOS_WALLETS_PATH`: Path for file with Aptos public addresses (each address from new line).

* **Trader Joe**
    * `TRADER_JOE_AMOUNT_FROM`: The lowest value to swap in `AVAX`;
    * `TRADER_JOE_AMOUNT_TO`: The highest value to swap in `AVAX`;
    * `TRADER_JOE_MAX_GAS`: If price for chain gas is higher than this value, the script will sleep 30 seconds and try again;
    * `TRADER_JOE_MAX_BTC`: Max value of BTC.b to swap in `BTC`.

* **Aptos Bridge**
    * `APTOS_AMOUNT_FROM`: The lowest value to bridge in `USDT`;
    * `APTOS_AMOUNT_TO`: The highest value to bridge in `USDT`;
    * `APTOS_SOURCE_CHAINS`: The script will choose source chain at random from this list. Possible choices: `Polygon`, `Arbitrum`, `BSC`;
    * `APTOS_MAX_GAS`: If price for chain gas is higher than this value, the script will sleep 30 seconds and try again;
    * `APTOS_MAX_VALUE`: If price for LayerZero gas is higher than this value, the script will sleep 30 seconds and try again.

* **Testnet Bridge**
    * `TESTNET_AMOUNT_FROM`: The lowest value to bridge in `ETH`;
    * `TESTNET_AMOUNT_TO`: The highest value to bridge in `ETH`;
    * `TESTNET_SOURCE_CHAINS`: The script will choose source chain at random from this list. Possible choices: `Arbitrum`, `Optimism`;
    * `TESTNET_MAX_GAS`: If price for chain gas is higher than this value, the script will sleep 30 seconds and try again;
    * `TESTNET_MAX_VALUE`: If price for LayerZero gas is higher than this value, the script will sleep 30 seconds and try again.

* **Harmony Bridge**
    * `HARMONY_AMOUNT_FROM`: The lowest value to bridge in `USDT`;
    * `HARMONY_AMOUNT_TO`: The highest value to bridge in `USDT`;
    * `HARMONY_SOURCE_CHAINS`: The script will choose source chain at random from this list. Possible choices: `BSC`;
    * `HARMONY_MAX_GAS`: If price for chain gas is higher than this value, the script will sleep 30 seconds and try again;
    * `HARMONY_MAX_VALUE`: If price for LayerZero gas is higher than this value, the script will sleep 30 seconds and try again.

* **Bitcoin Bridge**
    * `BITCOIN_BRIDGE_ALL`: If True, bridge all possible `BTC.b`;
    * `BITCOIN_AMOUNT_FROM`: The lowest value to bridge in `BTC.b` (if `BITCOIN_BRIDGE_ALL` is False);
    * `BITCOIN_AMOUNT_TO`: The highest value to bridge in `BTC.b` (if `BITCOIN_BRIDGE_ALL` is False);
    * `BITCOIN_SOURCE_CHAINS`: The script will choose source chain at random from this list. Possible choices: `Avalanche`, `Polygon`. Must add at least two chains;
    * `BITCOIN_MAX_GAS`: If price for chain gas is higher than this value, the script will sleep 30 seconds and try again;
    * `BITCOIN_MAX_VALUE`: If price for LayerZero gas is higher than this value, the script will sleep 30 seconds and try again.

* **Stargate Bridge**
    * `STARGATE_AMOUNT_FROM`: The lowest value to bridge in `USDT`;
    * `STARGATE_AMOUNT_TO`: The highest value to bridge in `USDT`;
    * `STARGATE_FROM_CHAINS`: The script will choose source chain at random from this list. Possible choices: `BSC`, `Arbitrum`, `Optimism`, `Polygon`, `Avalanche`, `Fantom`;
    * `STARGATE_TO_CHAINS`: The script will choose destination chain at random from this list. Possible choices: `BSC`, `Arbitrum`, `Optimism`, `Polygon`, `Avalanche`, `Fantom`;
    * `STARGATE_FROM_TOKENS`: The script will choose source token at random from this list. Possible choices: `BSC` (`USDT`), `Arbitrum` (`USDT`), `Optimism` (`USDC`), `Polygon` (`USDT` and `USDC`), `Avalanche` (`USDT` and `USDC`), `Fantom` (`USDC`);
    * `STARGATE_FROM_TOKENS`: The script will choose destination token at random from this list. Possible choices: `BSC` (`USDT`), `Arbitrum` (`USDT`), `Optimism` (`USDC`), `Polygon` (`USDT` and `USDC`), `Avalanche` (`USDT` and `USDC`), `Fantom` (`USDC`);
    * `STARGATE_MAX_GAS`: If price for chain gas is higher than this value, the script will sleep 30 seconds and try again;
    * `STARGATE_MAX_VALUE`: If price for LayerZero gas is higher than this value, the script will sleep 30 seconds and try again.
    * `STARGATE_SLIPPAGE`: Slippage for Stargate in %.

* **Merkly Refuel**
    * `MERKLY_FROM_CHAINS`: The script will choose source chain at random from this list. Possible choices: `optimism`, `bsc`, `arbitrum`, `polygon`, `zksync`, `avalanche`, `gnosis`, `fantom`, `nova`, `core`, `celo`, `moonbeam`, `moonriver`;
    * `MERKLY_TO_CHAINS`: The script will choose destination chain at random from certain list. Check manually which destination chains are possible for certain source chain at [Merkly](https://minter.merkly.com/gas);
    * `MERKLY_AMOUNTS`: The lowest and highest values to bridge in native token for each destination chain. Chack manually at [Merkly](https://minter.merkly.com/gas).

-----

</br>
</br>

Donation (EVM address): `0x34Ec371BA620e6C67A115a6794D44FED038Cc78C`
