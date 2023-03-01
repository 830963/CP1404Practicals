
def get_password():
    password = input("Enter your password: ")
    return password


def print_asterisk(password):
    for _ in range(0, len(password)):
        print('*', end='')


def main():
    password = get_password()
    length = 10
    print(f"Your password is Valid? {'yes!' if len(password) >= length else 'no!'}")
    print_asterisk(password)


main()