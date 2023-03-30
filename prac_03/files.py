def write():
    """Function used to write the name in name.txt"""
    name = input("Enter your name: ")
    out_file = open("name.txt", "w")
    out_file.write(name)
    out_file.close()


def read():
    """Function used to read the name from name.txt"""
    in_file = open("name.txt", "r")
    name = in_file.read()
    print(f"Your name is {name}")
    in_file.close()


def read_and_add():
    """Function to read and find the sum of the first two lines of number.txt"""
    in_file = open("numbers.txt", "r")
    line1 = int(in_file.readline())
    line2 = int(in_file.readline())
    result = line1 + line2
    print(result)
    in_file.close()


def read_and_add_all():
    """Function to read and find the sum of all the other numbers of number.txt"""
    in_file = open("numbers.txt", "r")
    total = 0
    for line in in_file:
        number = int(line)
        total += number
    print(total)
    in_file.close()


write()
read()
read_and_add()
read_and_add_all()
