#!/usr/bin/env python3
"""
Display security details: holding accounts, quantity, value, last price w/ date, asset class.
argparse can effectively replace click for building CLIs.
"""
import argparse
from piecash import Commodity
from gnucash_portfolio import BookAggregate
from pricedb import PriceDbApplication, PriceModel, SecuritySymbol


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

    # header
    print("    security            quantity  ")
    print("-------------------------------------------------------")

    shares = agg.get_num_shares()

    print(f"{security.namespace}:{security.mnemonic}, shares: {shares:,.2f}")

    # todo add all the info from the security details page in web ui,
    # prices, etc.
    avg_price = agg.get_avg_price()
    currency = agg.get_currency()
    print(f"Average price: {avg_price:.4f} {currency}")

    # last price
    prices_app = PriceDbApplication()
    sec_symbol = SecuritySymbol("", "")
    sec_symbol.parse(symbol)
    latest_price = prices_app.get_latest_price(sec_symbol)
    latest_price_date = latest_price.datum.to_iso_date_string()
    print(f"Latest price: {latest_price.value} {latest_price.currency} on {latest_price_date}")

    print("\n")

    print("Holding Accounts:")
    print("-----------------")

    for account in agg.accounts:
        balance = account.get_balance()
        print(f"{account.fullname}, {balance:,.2f}")

if __name__ == "__main__":
    main()
