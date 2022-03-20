from examples import custom_style_3
from PyInquirer import prompt

from app.core import BTC, ETH, Kraken
from app.database import DbInterface

from .base import BaseCommand


class CliCommandHandlers(BaseCommand):
    @staticmethod
    def add_btc_addrs(args):
        DbInterface.create_btc_addrs(args.addrs)

    @staticmethod
    def add_eth_addrs(args):
        DbInterface.create_eth_addrs(args.addrs)

    @staticmethod
    def add_kraken_keys(args):
        keys: list = [
            {
                "type": "input",
                "name": "api_key",
                "message": "Your Kraken API KEY: ",
            },
            {
                "type": "input",
                "name": "private_key",
                "message": "Your Kraken Private Key: ",
            },
        ]

        keys: dict = prompt(keys, style=custom_style_3)

        api_key: str = keys.get("api_key")
        private_key: str = keys.get("private_key")

        DbInterface.create_kraken_keys(api_key, private_key)

    @staticmethod
    async def display_btc_balance(args):
        user_selected_currency: str = BaseCommand.get_user_fiat_conversion_currency()

        DbInterface.get_all_btc_addresses()
        addresses: list = DbInterface.ALL_BTC_ADDRESSES

        await BTC.get_multiple_btc_balances(addresses, user_selected_currency)

    @staticmethod
    async def display_eth_balance(args):
        user_selected_currency: str = BaseCommand.get_user_fiat_conversion_currency()

        DbInterface.get_all_eth_addresses()
        addresses: list = DbInterface.ALL_ETH_ADDRESSES

        await ETH.get_multiple_eth_balances(addresses, user_selected_currency)

    @staticmethod
    def display_kraken_balance(args):
        DbInterface.get_kraken_keys()
        keys = DbInterface.KRAKEN_KEYS

        Kraken.get_kraken_user_balance(keys['api_key'], keys['private_key'])

    @staticmethod
    def setup_database(args):
        DbInterface.set_up_database_tables()
