"""
Trying to put the whole CLI in here.
It will allow listing all the available commands with options and parameters (if any).
The commands will invoke their respective modules.

Example: `gp-cli me blah -w yo -y`
"""
import argparse

def test(args):
    print(f"yo args: how={args.how}, what={args.what}, yes={args.yes}")

# 
parser: argparse.ArgumentParser = argparse.ArgumentParser()
parser.add_argument('--version', action='version', version='0.0.1')

subparsers = parser.add_subparsers()
parser_me: argparse.ArgumentParser = subparsers.add_parser("me")
parser_you: argparse.ArgumentParser = subparsers.add_parser("you")

# argument (required)
parser_me.add_argument("how", type=str, help="how?")
# option
parser_me.add_argument("-w", "--what", default="Nuffin'")
# flag
parser_me.add_argument("-y", "--yes", action="store_true")
parser_me.set_defaults(func=test)

if __name__ == "__main__":
    args = parser.parse_args()
    args.func(args)
