from brownie import Island_Manager, accounts, config, network
import time


def deploy_test(deploy, w1, w2, cap, price, nR, R, h):
    im = Island_Manager.deploy(
        w1, w2, cap, price, nR, R, h, {"from": deploy}, publish_source=False
    )
    time.sleep(2)
    return im


def deploy_my_acc(
    deploy_acc, nftMaxCap, nftPrice, notRevealedURL, revealedURL, rootHash
):
    withdrawacc = make_accounts(2)
    im = Island_Manager.deploy(
        withdrawacc[0].address,
        withdrawacc[1].address,
        nftMaxCap,
        nftPrice,
        notRevealedURL,
        revealedURL,
        rootHash,
        {"from": deploy_acc},
        publish_source=True,
    )
    # time.sleep(2)
    return im


def deploy_development(nftMaxCap, nftPrice, notRevealedURL, revealedURL, rootHash):
    withdrawacc = make_accounts(2)
    deploy_acc = make_accounts(1)[0]

    im = Island_Manager.deploy(
        withdrawacc[0].address,
        withdrawacc[1].address,
        nftMaxCap,
        nftPrice,
        notRevealedURL,
        revealedURL,
        rootHash,
        {"from": deploy_acc},
    )
    time.sleep(2)
    return im


def make_accounts(x):
    accs = []
    for i in range(x):
        accs.append(accounts.add())
    return accs


def create_files(num):
    path = "./addresses" + str(num)
    accs = []
    for i in range(num):
        accs.append(accounts.add().address)
    with open(path, "w+") as f:
        for item in accs:
            f.write(item + "\n")
    return path


def read_files(file):
    ret = []
    with open(file, "r") as f:
        ret = f.readlines()
    for i in range(len(ret)):
        ret[i] = ret[i][:-1]
    return ret
