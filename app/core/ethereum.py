import asyncio

from decouple import config
from web3 import Web3

from .utils import convert_between_currencies


class ETH(object):
    @staticmethod
    async def __get_eth_balance(eth_addr: str, target_currency: str = "USD") -> int:
        """
        You could either use a hosted or local node.
        To use a local node, set the env vars PROVIDER_URL, IS_LOCAL_NODE to your
        Local node's ipc path and True respectively
        """

        provider_url: str = config("PROVIDER_URL")

        if config(
            "IS_LOCAL_NODE", cast=bool
        ):  # Connect to local node via IPC --fast and secure
            w3: Web3 = Web3(Web3.IPCProvider(provider_url))
        else:
            w3: Web3 = Web3(Web3.HTTPProvider(provider_url))

        is_connected: bool = w3.isConnected()
        is_valid_address: bool = w3.isAddress(eth_addr)

        if is_connected and is_valid_address:
            # Web3.py only accepts checksums addresses
            balance: float = w3.eth.get_balance(w3.toChecksumAddress(eth_addr))

            # balance is returned in wei, convert to ETH
            balance: float = w3.fromWei(balance, "ether")

            # Get fiat equivalent of btc in target currency
            fiat_balance: float = await convert_between_currencies(
                balance, "ETH", target_currency
            )

            response: str = (
                f"Wallet Address: {eth_addr} \nETH Available: {balance}"
                f"\nETH Equivalent in {target_currency}: {fiat_balance}\n"
            )
            print(response)
        elif not is_valid_address:
            response: str = (
                f"Wallet Address: {eth_addr} \nERROR: invalid wallet address\n"
            )
            print(response)

    @classmethod
    async def get_multiple_eth_balances(cls, addrs: list, target_currency: str):
        funcs = []
        for addr in addrs:
            funcs.append(
                asyncio.ensure_future(cls.__get_eth_balance(addr, target_currency))
            )

        response = await asyncio.gather(*funcs)
        return response
