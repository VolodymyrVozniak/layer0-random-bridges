import os
import json


with open(os.path.join(os.path.dirname(__file__), "abi/erc20.json"), "r") as file:
    ERC20_ABI = json.load(file)

MAX_TIME_CHECK_TX_STATUS = 100

DATA = {
    'ethereum'      : {'rpc': 'https://rpc.ankr.com/eth', 'scan': 'https://etherscan.io/tx', 'token': 'ETH', 'chain_id': 1},

    'optimism'      : {'rpc': 'https://rpc.ankr.com/optimism', 'scan': 'https://optimistic.etherscan.io/tx', 'token': 'ETH', 'chain_id': 10},

    'bsc'           : {'rpc': 'https://rpc.ankr.com/bsc', 'scan': 'https://bscscan.com/tx', 'token': 'BNB', 'chain_id': 56},

    'polygon'       : {'rpc': 'https://rpc.ankr.com/polygon', 'scan': 'https://polygonscan.com/tx', 'token': 'MATIC', 'chain_id': 137},

    'polygon_zkevm' : {'rpc': 'https://zkevm-rpc.com', 'scan': 'https://zkevm.polygonscan.com/tx', 'token': 'ETH', 'chain_id': 1101},

    'arbitrum'      : {'rpc': 'https://rpc.ankr.com/arbitrum', 'scan': 'https://arbiscan.io/tx', 'token': 'ETH', 'chain_id': 42161},

    'avalanche'     : {'rpc': 'https://rpc.ankr.com/avalanche', 'scan': 'https://snowtrace.io/tx', 'token': 'AVAX', 'chain_id': 43114},

    'fantom'        : {'rpc': 'https://rpc.ankr.com/fantom', 'scan': 'https://ftmscan.com/tx', 'token': 'FTM', 'chain_id': 250},

    'nova'          : {'rpc': 'https://nova.arbitrum.io/rpc', 'scan': 'https://nova.arbiscan.io/tx', 'token': 'ETH', 'chain_id': 42170},

    'zksync'        : {'rpc': 'https://mainnet.era.zksync.io', 'scan': 'https://explorer.zksync.io/tx', 'token': 'ETH', 'chain_id': 324},
    
    'celo'          : {'rpc': 'https://1rpc.io/celo', 'scan': 'https://celoscan.io/tx', 'token': 'CELO', 'chain_id': 42220},

    'gnosis'        : {'rpc': 'https://rpc.ankr.com/gnosis', 'scan': 'https://gnosisscan.io/tx', 'token': 'xDAI', 'chain_id': 100},

    'core'          : {'rpc': 'https://rpc.coredao.org', 'scan': 'https://scan.coredao.org/tx', 'token': 'CORE', 'chain_id': 1116},

    'harmony'       : {'rpc': 'https://api.harmony.one', 'scan': 'https://explorer.harmony.one/tx', 'token': 'ONE', 'chain_id': 1666600000},

    'moonbeam'      : {'rpc': 'https://rpc.ankr.com/moonbeam', 'scan': 'https://moonscan.io/tx', 'token': 'GLMR', 'chain_id': 1284},

    'moonriver'     : {'rpc': 'https://moonriver.public.blastapi.io', 'scan': 'https://moonriver.moonscan.io/tx', 'token': 'MOVR', 'chain_id': 1285},
}

MERKLY_CONTRACTS = {
    'optimism'      : '0xa2c203d7ef78ed80810da8404090f926d67cd892',
    'bsc'           : '0xfdc9018af0e37abf89233554c937eb5068127080',
    'arbitrum'      : '0xaa58e77238f0e4a565343a89a79b4addd744d649',
    'polygon'       : '0xa184998ec58dc1da77a1f9f1e361541257a50cf4',
    # 'polygon_zkevm' : '', пока недоступен
    'zksync'        : '0x6dd28C2c5B91DD63b4d4E78EcAC7139878371768',
    'avalanche'     : '0xe030543b943bdcd6559711ec8d344389c66e1d56',
    'gnosis'        : '0xb58f5110855fbef7a715d325d60543e7d4c18143',
    'fantom'        : '0x97337a9710beb17b8d77ca9175defba5e9afe62e',
    'nova'          : '0x484c402b0c8254bd555b68827239bace7f491023',
    # 'harmony'       : '', # надо конвертировать в one-address
    'core'          : '0xCA230856343C300f0cc2Bd77C89F0fCBeDc45B0f',
    'celo'          : '0xe33519c400b8f040e73aeda2f45dfdd4634a7ca0',
    'moonbeam'      : '0x766b7aC73b0B33fc282BdE1929db023da1fe6458',
    'moonriver'     : '0x97337A9710BEB17b8D77cA9175dEFBA5e9AFE62e',
}

LAYERZERO_CHAINS_ID = {
    'avalanche' : 106,
    'polygon'   : 109,
    'ethereum'  : 101,
    'bsc'       : 102,
    'arbitrum'  : 110,
    'optimism'  : 111,
    'fantom'    : 112,
    'aptos'     : 108,
    'harmony'   : 116,
    'celo'      : 125,
    'moonbeam'  : 126,
    'fuse'      : 138,
    'gnosis'    : 145,
    'klaytn'    : 150,
    'metis'     : 151,
    'core'      : 153,
    'polygon_zkevm': 158,
    'canto'     : 159,
    'zksync'    : 165,
    'moonriver' : 167,
    'tenet'     : 173,
    'nova'      : 175,
    'kava'      : 177,
    'meter'     : 176,
}

ABI_MERKLY_REFUEL = '[{"inputs":[{"internalType":"uint256","name":"_minGasToTransfer","type":"uint256"},{"internalType":"address","name":"_layerZeroEndpoint","type":"address"},{"internalType":"uint256","name":"_startMintId","type":"uint256"},{"internalType":"uint256","name":"_endMintId","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bytes32","name":"_hashedPayload","type":"bytes32"}],"name":"CreditCleared","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bytes32","name":"_hashedPayload","type":"bytes32"},{"indexed":false,"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"CreditStored","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"indexed":false,"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"indexed":false,"internalType":"uint64","name":"_nonce","type":"uint64"},{"indexed":false,"internalType":"bytes","name":"_payload","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"_reason","type":"bytes"}],"name":"MessageFailed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"indexed":true,"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"indexed":true,"internalType":"address","name":"_toAddress","type":"address"},{"indexed":false,"internalType":"uint256[]","name":"_tokenIds","type":"uint256[]"}],"name":"ReceiveFromChain","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"indexed":false,"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"indexed":false,"internalType":"uint64","name":"_nonce","type":"uint64"},{"indexed":false,"internalType":"bytes32","name":"_payloadHash","type":"bytes32"}],"name":"RetryMessageSuccess","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"indexed":true,"internalType":"address","name":"_from","type":"address"},{"indexed":true,"internalType":"bytes","name":"_toAddress","type":"bytes"},{"indexed":false,"internalType":"uint256[]","name":"_tokenIds","type":"uint256[]"}],"name":"SendToChain","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"indexed":false,"internalType":"uint256","name":"_dstChainIdToBatchLimit","type":"uint256"}],"name":"SetDstChainIdToBatchLimit","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"indexed":false,"internalType":"uint256","name":"_dstChainIdToTransferGas","type":"uint256"}],"name":"SetDstChainIdToTransferGas","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"indexed":false,"internalType":"uint16","name":"_type","type":"uint16"},{"indexed":false,"internalType":"uint256","name":"_minDstGas","type":"uint256"}],"name":"SetMinDstGas","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_minGasToTransferAndStore","type":"uint256"}],"name":"SetMinGasToTransferAndStore","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"precrime","type":"address"}],"name":"SetPrecrime","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_remoteChainId","type":"uint16"},{"indexed":false,"internalType":"bytes","name":"_path","type":"bytes"}],"name":"SetTrustedRemote","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_remoteChainId","type":"uint16"},{"indexed":false,"internalType":"bytes","name":"_remoteAddress","type":"bytes"}],"name":"SetTrustedRemoteAddress","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DEFAULT_PAYLOAD_SIZE_LIMIT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"FUNCTION_TYPE_SEND","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"address","name":"_zroPaymentAddress","type":"address"},{"internalType":"bytes","name":"_adapterParams","type":"bytes"}],"name":"bridgeGas","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"clearCredits","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"}],"name":"dstChainIdToBatchLimit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"}],"name":"dstChainIdToTransferGas","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"bool","name":"_useZro","type":"bool"},{"internalType":"bytes","name":"_adapterParams","type":"bytes"}],"name":"estimateGasBridgeFee","outputs":[{"internalType":"uint256","name":"nativeFee","type":"uint256"},{"internalType":"uint256","name":"zroFee","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"bytes","name":"_toAddress","type":"bytes"},{"internalType":"uint256[]","name":"_tokenIds","type":"uint256[]"},{"internalType":"bool","name":"_useZro","type":"bool"},{"internalType":"bytes","name":"_adapterParams","type":"bytes"}],"name":"estimateSendBatchFee","outputs":[{"internalType":"uint256","name":"nativeFee","type":"uint256"},{"internalType":"uint256","name":"zroFee","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"bytes","name":"_toAddress","type":"bytes"},{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"bool","name":"_useZro","type":"bool"},{"internalType":"bytes","name":"_adapterParams","type":"bytes"}],"name":"estimateSendFee","outputs":[{"internalType":"uint256","name":"nativeFee","type":"uint256"},{"internalType":"uint256","name":"zroFee","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"bytes","name":"","type":"bytes"},{"internalType":"uint64","name":"","type":"uint64"}],"name":"failedMessages","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"fee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"}],"name":"forceResumeReceive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"},{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"_configType","type":"uint256"}],"name":"getConfig","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_remoteChainId","type":"uint16"}],"name":"getTrustedRemoteAddress","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"}],"name":"isTrustedRemote","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lzEndpoint","outputs":[{"internalType":"contract ILayerZeroEndpoint","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint64","name":"_nonce","type":"uint64"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"lzReceive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"maxMintId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"uint16","name":"","type":"uint16"}],"name":"minDstGasLookup","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minGasToTransferAndStore","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"mint","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"nextMintId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint64","name":"_nonce","type":"uint64"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"nonblockingLzReceive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"}],"name":"payloadSizeLimitLookup","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"precrime","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint64","name":"_nonce","type":"uint64"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"retryMessage","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"bytes","name":"_toAddress","type":"bytes"},{"internalType":"uint256[]","name":"_tokenIds","type":"uint256[]"},{"internalType":"address payable","name":"_refundAddress","type":"address"},{"internalType":"address","name":"_zroPaymentAddress","type":"address"},{"internalType":"bytes","name":"_adapterParams","type":"bytes"}],"name":"sendBatchFrom","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"bytes","name":"_toAddress","type":"bytes"},{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"address payable","name":"_refundAddress","type":"address"},{"internalType":"address","name":"_zroPaymentAddress","type":"address"},{"internalType":"bytes","name":"_adapterParams","type":"bytes"}],"name":"sendFrom","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"},{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"uint256","name":"_configType","type":"uint256"},{"internalType":"bytes","name":"_config","type":"bytes"}],"name":"setConfig","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint256","name":"_dstChainIdToBatchLimit","type":"uint256"}],"name":"setDstChainIdToBatchLimit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint256","name":"_dstChainIdToTransferGas","type":"uint256"}],"name":"setDstChainIdToTransferGas","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_fee","type":"uint256"}],"name":"setFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint16","name":"_packetType","type":"uint16"},{"internalType":"uint256","name":"_minGas","type":"uint256"}],"name":"setMinDstGas","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_minGasToTransferAndStore","type":"uint256"}],"name":"setMinGasToTransferAndStore","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint256","name":"_size","type":"uint256"}],"name":"setPayloadSizeLimit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_precrime","type":"address"}],"name":"setPrecrime","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"}],"name":"setReceiveVersion","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"}],"name":"setSendVersion","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_remoteChainId","type":"uint16"},{"internalType":"bytes","name":"_path","type":"bytes"}],"name":"setTrustedRemote","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_remoteChainId","type":"uint16"},{"internalType":"bytes","name":"_remoteAddress","type":"bytes"}],"name":"setTrustedRemoteAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"storedCredits","outputs":[{"internalType":"uint16","name":"srcChainId","type":"uint16"},{"internalType":"address","name":"toAddress","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"},{"internalType":"bool","name":"creditsRemain","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"}],"name":"trustedRemoteLookup","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"payable","type":"function"}]'
