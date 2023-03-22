import random

MIN_SCORE = 0
MID_SCORE = 50
HIGH_SCORE = 90
MAX_SCORE = 100


def get_score_result(score):
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    elif score >= HIGH_SCORE:
        return "Excellent"
    elif score >= MID_SCORE:
        return "Passable"
    else:
        return "Bad"


def main():
    user_score = float(input("Enter score: "))
    result = get_score_result(user_score)
    print(result)
    random_score = random.uniform(MIN_SCORE, MAX_SCORE)
    result = get_score_result(random_score)
    print(f"Random score ({random_score}): {result}")


main()
