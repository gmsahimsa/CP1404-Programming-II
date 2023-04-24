import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBER_PER_LINE = 6
NUM_QUICK_PICKS = 5


def main():
    num_quick_picks = get_num_of_quick_picks()
    for i in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        print_quick_pick(quick_pick)


def get_num_of_quick_picks():
    """Get the number of quick picks entered by the user"""
    num_quick_picks = int(input("How many quick picks? "))
    return num_quick_picks


def generate_quick_pick():
    """Generate the quick picks"""
    numbers = []
    while len(numbers) < NUMBER_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers


def print_quick_pick(numbers):
    """Print the quick picks"""
    for number in numbers:
        print("{:2d}".format(number), end=" ")
    print()


main()
