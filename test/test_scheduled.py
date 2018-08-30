""" Tests for scheduled transactions script """
from gnucash_portfolio_cli.gpcli import main


def test_creation():
    """ Call the cli and test scheduler tx script """
    main(arg1="blah")
