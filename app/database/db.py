import sqlite3

from .db_queries import (CREATE_CRYPTO_ADDRESS_TABLE, CREATE_KRAKEN_KEYS_TABLE,
                         FILTER_ADDRESSES_BY_TYPE, INSERT_BTC_ADDRESSES,
                         INSERT_ETH_ADDRESSES, INSERT_KRAKEN_KEYS,
                         RETRIEVE_KRAKEN_KEYS)


class DbInterface(object):
    ALL_BTC_ADDRESSES = None
    ALL_ETH_ADDRESSES = None
    KRAKEN_KEYS = None

    @staticmethod
    def __connection():
        try:
            con = sqlite3.connect("crypto.db")
            return con
        except Exception as e:
            print(e)

    @staticmethod
    def __query_executor_destructive(db_connection, query: str) -> None:
        """
        solely for running destructive queries-- create, update etc.
        Returns nothing
        """
        con = db_connection
        cur = con.cursor()
        cur.execute(query)

    @classmethod
    def set_up_database_tables(cls) -> None:
        con = cls.__connection()

        # Create crypto address table
        cls.__query_executor_destructive(con, CREATE_CRYPTO_ADDRESS_TABLE)

        # Create kraken keys table
        cls.__query_executor_destructive(con, CREATE_KRAKEN_KEYS_TABLE)

        con.commit()
        con.close()

    @classmethod
    def create_btc_addrs(cls, addrs: list) -> None:
        con = cls.__connection()
        cur = con.cursor()

        for addr in addrs:
            cur.execute(INSERT_BTC_ADDRESSES, (addr,))

        con.commit()
        con.close()
        print("\nAll your addresses added to database\n")

    @classmethod
    def create_eth_addrs(cls, addrs: list) -> None:
        con = cls.__connection()
        cur = con.cursor()

        for addr in addrs:
            cur.execute(INSERT_ETH_ADDRESSES, (addr,))

        con.commit()
        con.close()
        print("\nAll your addresses added to database\n")

    @classmethod
    def create_kraken_keys(cls, api_key: str, private_key) -> None:
        con = cls.__connection()
        cur = con.cursor()

        cur.execute(INSERT_KRAKEN_KEYS, (api_key, private_key))

        con.commit()
        con.close()
        print("\nAll your keys added to database\n")

    @classmethod
    def get_all_btc_addresses(cls) -> None:
        con = cls.__connection()
        cur = con.cursor()

        cur.execute(FILTER_ADDRESSES_BY_TYPE, {"typ": "BTC"})

        cls.ALL_BTC_ADDRESSES = [
            i[0] for i in cur.fetchall()
        ]  # Get only the address fields
        con.close()

    @classmethod
    def get_all_eth_addresses(cls) -> None:
        con = cls.__connection()
        cur = con.cursor()

        cur.execute(FILTER_ADDRESSES_BY_TYPE, {"typ": "ETH"})

        cls.ALL_ETH_ADDRESSES = [
            i[0] for i in cur.fetchall()
        ]  # Get only the address fields
        con.close()

    @classmethod
    def get_kraken_keys(cls) -> None:
        con = cls.__connection()
        cur = con.cursor()

        cur.execute(RETRIEVE_KRAKEN_KEYS)
        queryset = cur.fetchone()
        cls.KRAKEN_KEYS = {"api_key": queryset[0], "private_key": queryset[1]}
        con.close()
