import argparse

from passgen import __version__


def parse_flags():
    """Method created to parse up the CLI flags beforehand."""
    parser = argparse.ArgumentParser(
        prog='passgen',
        description='%(prog)s - generate a random password easily.'
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'%(prog)s {__version__}'
    )
    parser.add_argument(
        '-n', '--numbers',
        default=False,
        action='store_true',
        help='Whether to include numbers.'
    )
    parser.add_argument(
        '-uc', '--upper-case',
        default=False,
        action='store_true',
        help='Whether to include uppercase letters.',
    )
    parser.add_argument(
        '-sc', '--special-characters',
        default=False,
        action='store_true',
        help='Whether to include special characters.',
    )
    return parser.parse_args()
