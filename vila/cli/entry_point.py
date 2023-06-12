import sys
from argparse import ArgumentParser

from .cmd_init import initialize_environment
from .cmd_start import start_bot
from .. import constants


def main():
    if len(sys.argv) == 1:
        start_bot()
        return

    parser = ArgumentParser(prog=constants.NAME, description='%s CLI' % constants.NAME)
    parser.add_argument('-V', '--version', help='Print %s version and exit' % constants.NAME, action='store_true')
    subparsers = parser.add_subparsers(title='command', help='Available commands', dest='subparser_name')

    subparsers.add_parser('start', help='Start %s' % constants.NAME)
    subparsers.add_parser('init', help='Prepare environment for %s' % constants.NAME)

    args = parser.parse_args()

    if args.version:
        print('%s %s' % (constants.NAME, constants.VERSION))
        return

    if args.subparser_name == 'start':
        start_bot()
    elif args.subparser_name == 'init':
        initialize_environment()
