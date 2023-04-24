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


def get_valid_score():
    while True:
        score_str = input("Enter a score between 0 and 100 (inclusive): ")
        try:
            score = float(score_str)
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except:
            print("Invalid input, please enter a number.")


def print_result(score):
    result = get_result(score)
    print(f"Score result: {result}")


def show_stars(score):
    stars = "*" * int(score)
    print(stars)


def main():
    score = get_valid_score()
    MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    choice = ""

    while choice.upper() != "Q":
        print(MENU)
        choice = input("Enter your choice: ")

        if choice.upper() == "G":
            score = get_valid_score()
        elif choice.upper() == "P":
            if score is None:
                print("No score has been entered yet.")
            else:
                print_result(score)
        elif choice.upper() == "S":
            if score is None:
                print("No score has been entered yet.")
            else:
                show_stars(score)
        elif choice.upper() == "Q":
            print("Have a nice day!")
        else:
            print("Invalid choice. Please try again.")


main()
