import random
import argparse

parser = argparse.ArgumentParser(
    description='Clarify your specific parameters!'
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

args = parser.parse_args()


def generate_password(length: int = 25) -> str:
    """The core of this module, generates a random password for you.

    Args:
        length (int, optional): Length of the password. Defaults to 25.

    Returns:
        str: Randomly generated password due to your parameters."""

    LOWERCASE = 'qwertyuiopasdfghjklzxcvbnm'
    NUMBERS = '1234567890'
    UPPERCASE = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    SPECIAL = '!@#$%^&*()'

    if args.numbers:
        LOWERCASE += NUMBERS

    if args.upper_case:
        LOWERCASE += UPPERCASE

    if args.special_characters:
        LOWERCASE += SPECIAL

    result = random.choices(LOWERCASE, k=length)
    return ''.join(result)
