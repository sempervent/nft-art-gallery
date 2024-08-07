from web3 import Web3
import os
import json


def load_wallet():
    path_to_key = os.getenv("WALLET_KEY_PATH")
    with open(path_to_key) as key_file:
        key_data = json.load(key_file)
        return key_data["private_key"]


def get_account():
    w3 = Web3(Web3.HTTPProvider(os.getenv("BLOCKCHAIN_PROVIDER_URL")))
    private_key = load_wallet()
    account = w3.eth.account.privateKeyToAccount(private_key)
    return account


# Example Usage
# account = get_account()
# print(account.address)
