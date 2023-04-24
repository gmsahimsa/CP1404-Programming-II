"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Question
# When will a ValueError occur? - if the user inputs a non-integer value for number
# When will a ZeroDivisionError occur? - if the user inputs 0 for number
# Could you change the code to avoid the possibility of a ZeroDivisionError? -
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
