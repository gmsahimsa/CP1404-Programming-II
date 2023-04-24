"""
2. Debugging:
CP1404/CP5632 - Practical
Broken program to determine score status
"""
MIN_SCORE = 0
MID_SCORE = 50
HIGH_SCORE = 90
MAX_SCORE = 100
score = float(input("Enter score: "))
if score < MIN_SCORE or score > MAX_SCORE:
    print("Invalid score")
elif score >= HIGH_SCORE:
    print("Excellent")
elif score >= MID_SCORE:
    print("Passable")
else:
    print("Bad")
