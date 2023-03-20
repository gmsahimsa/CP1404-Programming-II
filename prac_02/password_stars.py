def get_password():

    MIN_LENGTH = 8
    password = input("Enter a password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input("Enter a password: ")
    return password


def print_asterisks(password):
    print("*" * len(password))


def main():
    password = get_password()
    print_asterisks(password)


main()
