#!/usr/bin/env python3
"""
Display security details: holding accounts, quantity, value, last price w/ date, asset class.
argparse can effectively replace click for building CLIs.
"""
import argparse
from piecash import Commodity
from gnucash_portfolio import BookAggregate

def read_parameters():
    """ Read parameters from the command line """
    parser = argparse.ArgumentParser(description='read symbol from command line')
    parser.add_argument('symbol', type=str, help='security symbol')
    args = parser.parse_args()
    return args

def main():
    args = read_parameters()
    symbol = args.symbol
    symbol = symbol.upper()

    book = BookAggregate()

    agg = book.securities.get_aggregate_for_symbol(symbol)
    security = agg.security

    # Display
    if security is None:
        print(f"No securities found for {symbol}.")
        exit

    shares = agg.get_num_shares()

    print(f"{security.namespace}:{security.mnemonic}, shares: {shares}")

    for account in agg.accounts:
        balance = account.get_balance()
        print(f"{account.fullname}, {balance}")

if __name__ == "__main__":
    main()
