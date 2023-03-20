import random

MINIMUM_SCORE = 0
MID_SCORE = 50
HIGH_SCORE = 90
MAXIMUM_SCORE = 100


def get_result(score):

    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    elif score >= HIGH_SCORE:
        return "Excellent"
    elif score >= MID_SCORE:
        return "Passable"
    else:
        return "Bad"


def main():
    user_input_score = float(input("Enter Your Score: "))
    print(get_result(user_input_score))
    random_score = random.uniform(0, 100)
    print(f"Random score Generated: {random_score}")
    print(get_result(random_score))


main()
