from password_generator import LengthNotInRange, generate_password

length = int(input('Enter whatever length you want: '))

if not 4 <= length <= 50:
    raise LengthNotInRange(length)

print(generate_password(length=length))
