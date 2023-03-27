from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000

# Python3 code to convert a tuple
# into a string using str.join() method
def convertTuple(tup):
    str = "".join(tup)
    return str


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])  # load from .env


def deploy_mocks():
    print(f"The acive network is {network.show_active()}")
    print(f"Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:  # only deploy if not already deployed
        mock_aggregator = MockV3Aggregator.deploy(
            # DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()}
            # Updates code: https://youtu.be/M576WGiDBdQ?t=20633
            DECIMALS,
            STARTING_PRICE,
            {"from": get_account()},
        )
    price_feed_address = MockV3Aggregator[-1].address
    print(f"Mocks Deployed...")
