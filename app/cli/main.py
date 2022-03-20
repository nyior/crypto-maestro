import argparse

from .command_handlers import CliCommandHandlers


async def main_cli():
    parser = argparse.ArgumentParser(prog="python main.py")
    subparsers = parser.add_subparsers()

    # Add BTC Addresses command parser: adds btc addresses to db
    add_btc = subparsers.add_parser("add-adrs-btc")
    add_btc.add_argument(
        "addrs",
        nargs="*",  # Accepts one or more btc addresses
        help="BTC addreses to be saved",
    )
    add_btc.set_defaults(
        func=CliCommandHandlers.add_btc_addrs
    )  # Default function to be invoked

    # Add ETH Addresses command parser: adds eth addrs to db
    add_eth = subparsers.add_parser("add-adrs-eth")
    add_eth.add_argument(
        "addrs",
        nargs="*",  # Accepts one or more eth addresses
        help="nETH addresses to be saved to db",
    )
    add_eth.set_defaults(func=CliCommandHandlers.add_eth_addrs)

    # Add kraken creds command parser: adds kraken api $ private keys to db
    add_kraken_keys = subparsers.add_parser("add-kraken-keys")
    add_kraken_keys.set_defaults(func=CliCommandHandlers.add_kraken_keys)

    # Display BTC balance command parser
    btc_balance = subparsers.add_parser("display_balance_btc")
    btc_balance.set_defaults(func=CliCommandHandlers.display_btc_balance)

    # Display ETH balance command parser
    eth_balance = subparsers.add_parser("display-balance-eth")
    eth_balance.set_defaults(func=CliCommandHandlers.display_eth_balance)

    # Display Kraken balance command parser
    kraken_balance = subparsers.add_parser("display-balance-kraken")
    kraken_balance.set_defaults(func=CliCommandHandlers.display_kraken_balance)

    # Create database tables
    setup_database = subparsers.add_parser("setup-db")
    setup_database.set_defaults(func=CliCommandHandlers.setup_database)

    args = parser.parse_args()

    # Await asynchronous functions
    if (
        args.func.__name__ == "display_btc_balance"
        or args.func.__name__ == "display_eth_balance"
    ):
        await args.func(args)  # Invoke whatever function was selected async
    else:
        args.func(args)  # sync
