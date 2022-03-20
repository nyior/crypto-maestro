import asyncio

from decouple import config

from .utils import convert_between_currencies, query_external_service_async


class BTC(object):
    @staticmethod
    async def __get_btc_balance(btc_addr: str, target_currency: str = "USD") -> None:
        URL: str = config("BLOCK_CYPHER_URL")
        URL: str = URL.format(btc_addr)

        response: dict = await query_external_service_async(URL)
        if "balance" in response:
            balance: float = response["balance"]

            # balance is in satoshis, convert to BTC``
            balance: float = balance / 100000000

            # Get fiat equivalent of btc in target currency
            fiat_balance: float = await convert_between_currencies(
                balance, "BTC", target_currency
            )

            balance_statement: str = (
                f"Wallet Address: {btc_addr} \nBTC Available: {balance}"
                f"\nBTC Equivalent in {target_currency}: {fiat_balance}\n"
            )
            print(balance_statement)
        else:
            error_statement: str = (
                f"\nWallet Address: {btc_addr} \nError: {response['error']}\n"
            )
            print(error_statement)

    @classmethod
    async def get_multiple_btc_balances(cls, addrs: list, target_currency: str):
        funcs = []
        for addr in addrs:
            funcs.append(
                asyncio.ensure_future(cls.__get_btc_balance(addr, target_currency))
            )

        response = await asyncio.gather(*funcs)
        return response
