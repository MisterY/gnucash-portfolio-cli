"""
Trying to put the whole CLI in here.
It will allow listing all the available commands with options and parameters (if any).
The commands will invoke their respective modules.

Example: `gp-cli test blah -w yo -y`
"""
import argparse

def show(args):
    print(f"yo args: what={args.what}, why={args.why}, yes={args.yes}")

def main():
    """ this code is in a function so that it can be declared an entry point in setup.py """
    args = parser.parse_args()
    if isinstance(args, argparse.Namespace):
        #args = parser.parse_args(["-h"])
        args = parser.parse_args(["test", "me"])

    args.func(args)

# 
parser: argparse.ArgumentParser = argparse.ArgumentParser()
parser.add_argument('--version', action='version', version='0.0.1')

subparsers = parser.add_subparsers()
parser_me: argparse.ArgumentParser = subparsers.add_parser("test")
parser_you: argparse.ArgumentParser = subparsers.add_parser("secinfo")

# argument (required)
parser_me.add_argument("what", type=str, help="test what?")
# option
parser_me.add_argument("-w", "--why", default="because!")
# flag
parser_me.add_argument("-y", "--yes", action="store_true")
parser_me.set_defaults(func=show)

if __name__ == "__main__":
    main()
