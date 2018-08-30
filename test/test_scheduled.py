""" Tests for scheduled transactions script """
from gnucash_portfolio_cli import gpcli


def test_creation():
    """ Call the cli and test scheduler tx script """
    gpcli.main("scheduled")
