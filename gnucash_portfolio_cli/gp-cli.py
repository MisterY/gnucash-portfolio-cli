"""
Trying to put the whole CLI in here.
It will allow listing all the available commands with options and parameters (if any).
The commands will invoke their respective modules.

Example: `gp-cli test me -w yo -y`
"""
import argparse
from gnucash_portfolio_cli import security_info


def show(args):
    print(f"yo args: what={args.what}, why={args.why}, yes={args.yes}")

def main():
    """ this code is in a function so that it can be declared an entry point in setup.py """
    args = parser.parse_args()
    if isinstance(args, argparse.Namespace):
        args = parser.parse_args(["secinfo", "vym"])
        #args = parser.parse_args(["-h"])
        #args = parser.parse_args(["test", "me"])

    args.func(args)

# 
parser: argparse.ArgumentParser = argparse.ArgumentParser()
parser.add_argument('--version', action='version', version='0.0.1')

subparsers = parser.add_subparsers()
parser_test: argparse.ArgumentParser = subparsers.add_parser("test")
parser_secinfo: argparse.ArgumentParser = subparsers.add_parser("secinfo")

# argument (required)
parser_test.add_argument("what", type=str, help="test what?")
# option
parser_test.add_argument("-w", "--why", default="because!")
# flag
parser_test.add_argument("-y", "--yes", action="store_true")
parser_test.set_defaults(func=show)

# Security Info
parser_secinfo.add_argument("symbol", type=str, help="Security symbol to provide the information for")
parser_secinfo.set_defaults(func=security_info.run)

if __name__ == "__main__":
    main()
