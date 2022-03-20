<h1>
	CLI Tool for Looking up Useful Data of a Crypto Address.
</h1>

## What is this about?
It's a minimal CLI tool that connects to the ethereum, and bitcoin blochains as well as the Kraken Exchange.

## Features 
Here are some the things you could do with this tool:
- Register 1 or more BTC Addresses
- Register 1 or more ETH Addresses
- Register a Kraken API key with its associated private key

Note that registration here entails submitting the above listed data and having the CLI
tool persist those data. I used the SQLite3 DB for data persistence. Pardon the deviation :))
Speaking of features:

- Get the baalances of all the BTC addresses at a go: Here the balance is returned in BTC and one of 5 Fiat Currencies(USD, EUR, NGN, CNY, JPY). The user gets to pick whichever currency they
- Get the baalances of all the ETH addresses at a go: same impplementation as the previous one.
- Retrieve the balances of a Kranken account given its private key and associated api-key.

Note that for quering the ethereum blochain, you could either go with a hosted provider or local node. More on this shortly.


## Getting Started Locally
To set this project up locally and test it out follow the following steps:
- Clone this repo to your local machine
- Create a virtual env for the project
- Navigate to the project's root directory and install all the dependencies `pip install requirements.txt`
- For Ethereum queries, if you'd rather have the system query your local node, update the `PROVIDER_URL` environment variable in the `.env` file to your local node's IPC's path and set `IS_LOCAL_NODE` to `True`


## Accessing the Features
Being a CLI program, you can only access the features of this project via the command line.
You do that by navigating to the project's root directory that would then trigger certain
actions by the system. All commands are preceeded by `python main.py`.

#### First Step
The very first step you need to take is runnning the command that would setup a local sqlite
database with all the required tables.
- Run the command `python main.py setup-db`

#### Adding BTC Addresses
- Run the command `python main.py add-adrs-btc addrs1 addrs2 ... addrs-n`

#### Adding ETH Addresses
- Run the command `python main.py add-adrs-eth addrs1 addrs2 ... addrs-n`

#### Adding Kraken keys
- Run the command `python main.py add-kraken-keys`
    - The user will then be prompted to type in their api, and private keys

All the above inputs are then saved in the sqlite database that has been setup in the first step.

#### Getting  BTC Balances
- Run the command `python main.py display-balance-btc`
    - The user will then be prompted to pick the fiat currency they'd want the system to show
    The their fiat balance

#### Getting ETH Balances
- Run the command `python main.py display-balance-eth`
    - The user will be prompted again for currency

#### Getting Kranke Balances
- Run the command `python main.py display-balance-kranken`

#### Getting Help
- Run the command `python main.py -h` 
    - This will show a list of all the available commands. Sadly, I haven't added descriptions for ths command. It's meant to serve as a list that you could always refer to

