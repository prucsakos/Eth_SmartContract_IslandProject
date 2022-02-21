import brownie
from scripts.utils import *
from brownie import Island_Manager, accounts, network, config


deploy_acc = accounts.add(config["wallets"]["riskby_from_key"])
w1 = accounts.add()
w2 = accounts.add()
price = 10000000000000000
nftCap = 8888
nR = "https://youtube.com/"
R = "https://facebook.com/"
h = "0ac24f1e3582c9ee6ec61f9897949bd229ff3cf55f56d5d591f20c73040ca95f"
proof = [
    "0x43d8919c9529351df3f50cc0759e12b2bd50534b9e2c20b0150d69def337af63",
    "0x1ff1d56a49a399243baa2c6c15eeee7db873d9624e21860c212304d13997b81a",
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


def test_basicDeploy():
    im = deploy_test(deploy_acc, w1.address, w2.address, nftCap, price, nR, R, h)
    assert im.CurrentStage({"from": deploy_acc}) == "NotStarted"
    im.goNextStage({"from": deploy_acc})
    assert im.CurrentStage({"from": deploy_acc}) == "OnlyWhitelistMint"
    im.goNextStage({"from": deploy_acc})
    assert im.CurrentStage({"from": deploy_acc}) == "PublicMint"
    im.goNextStage({"from": deploy_acc})
    assert im.CurrentStage({"from": deploy_acc}) == "Revealed"


def test_whiteList():
    im = deploy_test(deploy_acc, w1.address, w2.address, nftCap, price, nR, R, h)

    assert im.isOnWhitelist(deploy_acc.address, proof, {"from": deploy_acc})
    assert not (im.isOnWhitelist(w1.address, proof, {"from": w1}))
    assert not (im.isOnWhitelist(w2.address, proof, {"from": w2}))
    assert im.isAWithdrawal(w1.address, {"from": w1})
    assert im.isAWithdrawal(w2.address, {"from": w2})
    assert not im.isAWithdrawal(deploy_acc.address, {"from": deploy_acc})
