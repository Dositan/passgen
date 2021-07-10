from .cli import parse_flags
from .exceptions import LengthNotInRange
from .utils import generate_password


def main():
    """The main function of the password generator.

    Raises:
        LengthNotInRange: When the given length did not follow limits.
    """
    args = parse_flags()
    length = int(input('Enter whatever length you want: '))

    if not 4 <= length <= 50:
        raise LengthNotInRange(length)

    print(generate_password(length, args=args))


if __name__ == '__main__':
    main()
