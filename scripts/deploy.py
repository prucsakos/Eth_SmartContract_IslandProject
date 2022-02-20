from brownie import accounts, Island_Manager
from scripts.utils import *
import time


#   CONSTRUCTOR PARAMETERS
#        address param_whitdrawAddr1,
#        address param_whitdrawAddr2,
#        uint256 param_maxNftCap,
#        uint256 param_eth_mint_price,
#        string memory param_notRevealedURL,
#        string memory param_revealedURL,
#        bytes32 param_root_hash

TEST_PROOF = [
    "0x3033516196f97bd60f5ea789336343283d8a4792417230601ef787d20ba536a6",
    "0x836fffed7f86252811ddec39d78092f1fa7c46015e04afaec3194e3d53f1a008",
    "0xa67dbc7bc55ad2331d230fa64298349521a6bfc3ca159a6a52f4fc513faad219",
    "0x6c22d2b7e07bdee06e5d4e14a4d422dbbaa2c704a41760d13f41109fd08ba73e",
    "0x69c540eb9c6284e9d7b48a4cabc973f64adeacc89b9cc45bc92d04947b9e5c19",
    "0x553ba0b4aa2381b7b584e36021e2cbb65a4e2034398d2b007008af83a3f384f8",
    "0x890ba4609d8ed3b76c4ce3b6147e4f6bfe32516bb8fc990f827aed40be6de6b4",
    "0xfccf1deeebc1abcd511f0f73692aca74563e24625b58283ee380d83b95420704",
    "0x6d57567949bfee6345b9d54a1c21755514d0d6a3c3e1977d6dd39bf23a0b100b",
    "0xac6a5e0f78a4c1fbe524ee84ed46b3507ef935f8bc700307406a6fb861dfdaac",
    "0xae0af4e955f04f8d818520a878eed30077ab003cc96040b7ad3641f9cd30c9b8",
    "0x07a26ba4212ecf5fd9f709970872b9ad3f9b3783a1ccef57b96aaee24902a8b0",
]
TEST_ADDR = "0x053f547A0D701829064552d651CaaAD583520469"
# id/pw: test1/test1


def main():
    w1 = "0x6fB4D4A45BF2774d47199C0Be9fe7984A3153C2E"
    w2 = "0xCb0c12dB788a140Ab5102F23fdAd916E7e47C613"
    nftMaxCap = 8888
    eth = 100000000000000000  # 0.1 eth
    notRevealedUrl = "https://youtube.com/"
    revealedUrl = "https://facebook.com/"
    deploy_acc = accounts.add(config["wallets"]["riskby_from_key"])
    im = deploy_test(
        deploy_acc,
        w1,
        w2,
        cap=nftMaxCap,
        price=eth,
        nR=notRevealedUrl,
        R=revealedUrl,
        h="0ac24f1e3582c9ee6ec61f9897949bd229ff3cf55f56d5d591f20c73040ca95f",
    )
    time.sleep(1)
