import random
import string
from argparse import Namespace


def generate_password(length: int = 25, *, args: Namespace) -> str:
    """The core of this project, generates a random password according to

    the parsed parameters from client-side (CLI flags).

    Parameters
    ----------
    args : Namespace
        The namespace of arguments AKA flags, that get passed from the terminal.
    length : int, optional
        The length for the password creation, by default 25

    Returns
    -------
    str
        The final generated password.
    """
    CURRENT = string.ascii_lowercase

    if args.numbers:
        CURRENT += string.digits
    if args.upper_case:
        CURRENT += string.ascii_uppercase
    if args.special_characters:
        CURRENT += string.punctuation

    result = random.sample(CURRENT, length)
    return ''.join(result)
