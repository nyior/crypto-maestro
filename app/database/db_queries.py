CREATE_CRYPTO_ADDRESS_TABLE = """
                                create table crypto_address (
                                    address text not null primary key, 
                                    type text not null
                                )
                            """

CREATE_KRAKEN_KEYS_TABLE = """
                                create table kraken_keys (
                                    api_key text not null primary key, 
                                    private_key text not null unique
                                )
                            """

INSERT_BTC_ADDRESSES = 'insert into crypto_address values (?, "BTC")'
INSERT_ETH_ADDRESSES = 'insert into crypto_address values (?, "ETH")'

# type is one of btc or eth
FILTER_ADDRESSES_BY_TYPE = "select * from crypto_address where type=:typ"

INSERT_KRAKEN_KEYS = "insert into kraken_keys values (?, ?)"
# Since the user can only have one pair of keys, we just get everything
RETRIEVE_KRAKEN_KEYS = "select * from kraken_keys"
