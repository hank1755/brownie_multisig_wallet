from brownie import accounts, network, web3
from web3 import Web3
from eth_account import Account
from eth_account.messages import encode_defunct

# from eth_typing import HexStr
import os
from dotenv import load_dotenv
from scripts.utilities import get_account, convertTuple


def sign_eip191():
    # Get signer address
    signer = accounts[0]
    msg = f"This message is signed by address: {signer}"
    print(f"msg: {msg}")

    # Convert the message to bytes and hash it
    msg_hash = encode_defunct(text=msg)
    print(f"msg_hash: {msg_hash}")

    # Sign the msg_hash
    sign_msg = Account.sign_message(msg_hash, os.getenv("PRIVATE_KEY"))
    sign_msg = tuple(sign_msg)
    print(f"sign_msg: {sign_msg}")
    print(f"type(sign_msg): {type(sign_msg)}")

    # split signature
    r = sign_msg[1]
    print(f"r: {r}")
    s = "0x" + str(sign_msg[2])
    print(f"s: {s}")
    v = sign_msg[3]
    print(f"v: {v}")
    signature = sign_msg[4]
    print(f"signature: {signature}")


def main():
    sign_eip191()
