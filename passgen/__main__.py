from passgen.cli import parse_flags
from passgen.utils import generate_password


def main():
    """The main function of passgen."""
    args = parse_flags()
    length = int(input("Enter whatever length you want: "))

    print(generate_password(length, args))


if __name__ == "__main__":
    main()
