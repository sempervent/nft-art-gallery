import json
from web3 import Web3
from solcx import compile_source
from web3.contract import ConciseContract


class BlockchainInterface:
    def __init__(self, provider_url, contract_address, abi):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        self.contract = self.w3.eth.contract(address=contract_address, abi=abi)

    def get_all_art(self):
        return self.contract.functions.getAllArt().call()

    def mint_art(self, title, description, image_url, price):
        # This method should handle minting new art on the blockchain
        # For simplicity, we're assuming the function exists in your Solidity contract
        account = self.w3.eth.account.privateKeyToAccount(
            PRIVATE_KEY
        )  # Ensure the private key is securely managed
        nonce = self.w3.eth.getTransactionCount(account.address)
        transaction = self.contract.functions.mintArt(
            title, description, image_url, price
        ).buildTransaction(
            {
                "chainId": 1,  # Make sure to use the correct chain ID
                "gas": 2000000,
                "gasPrice": self.w3.toWei("10", "gwei"),
                "nonce": nonce,
            }
        )
        signed_txn = self.w3.eth.account.signTransaction(
            transaction, private_key=account.privateKey
        )
        return self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)


class ContractManager:
    def __init__(self, provider_url: str, contract_source: str):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        self.contract_source = contract_source
        self.contract = None

    def deploy_contract(self, account):
        compiled_sol = compile_source(self.contract_source)
        contract_interface = compiled_sol["<standard-json-output>"]
        Contract = self.w3.eth.contract(
            abi=contract_interface["abi"], bytecode=contract_interface["bin"]
        )
        tx_hash = Contract.constructor().transact({"from": account})
        tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
        self.contract = self.w3.eth.contract(
            address=tx_receipt.contractAddress,
            abi=contract_interface["abi"],
        )

    def interact_with_contract(self, function_name: str, *args, **kwargs):
        func = getattr(self.contract.functions, function_name)
        return func(*args, **kwargs).call()


# Example Usage
# manager = ContractManager('http://localhost:8545', 'source_code_here')
# manager.deploy_contract('your_account_address_here')
# result = manager.interact_with_contract('function_name_here', 'arguments_here')
