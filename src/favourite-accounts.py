#!/usr/bin/env python3
""" List your favorite accounts """

from pydatum import Datum
from gnucash_portfolio import BookAggregate

def main():
    """ Show the list of favorite accounts """
    print("Favourite accounts:\n")
    book = BookAggregate()
    favourites = book.accounts.get_favourite_account_aggregates()
    favourites = sorted(favourites, key=lambda aggregate: aggregate.account.name)

    for aggregate in favourites:
        # get details
        #balance = aggregate.get_balance()

        balance = aggregate.get_balance_on()
        print(f"{aggregate.account.name}, {balance}")

    print("\n")

if __name__ == "__main__":
    main()
