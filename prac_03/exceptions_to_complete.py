"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # TODO: Add the code to set is_finished to True if a valid integer is entered
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
