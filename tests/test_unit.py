import brownie
from scripts.utils import *
from brownie import Island_Manager, accounts, network, config


deploy_acc = accounts.add()
w1 = accounts.add()
w2 = accounts.add()
price = 10000000000000000
nftCap = 8888
nR = "https://youtube.com/"
R = "https://facebook.com/"
h = "5282540ec91c540243635ec3598d289cfaa283d7eea6b8f8498f61ad221259ac"


def test():
    assert 1 == 1
    assert 2 == 2


def test_basicDeploy():
    im = deploy_test(deploy_acc, w1.address, w2.address, nftCap, price, nR, R, h)
    assert im.CurrentStage({"from": deploy_acc}) == "NotStarted"
    im.nextStage({"from": deploy_acc})
    assert im.CurrentStage({"from": deploy_acc}) == "OnlyWhitelistMint"
    im.nextStage({"from": deploy_acc})
    assert im.CurrentStage({"from": deploy_acc}) == "PublicMint"
    im.nextStage({"from": deploy_acc})
    assert im.CurrentStage({"from": deploy_acc}) == "Revealed"
