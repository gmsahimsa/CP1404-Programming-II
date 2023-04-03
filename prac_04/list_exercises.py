TOTAL_NUMBER_OF_INPUT = 5
numbers = []
in_usernames = False
for i in range(TOTAL_NUMBER_OF_INPUT):
    input_number = input("Number: ")
    numbers.append(input_number)
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[len(numbers) - 1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
# print("The average of the numbers is", sum(numbers) / len(numbers))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
input_username = input("Enter Your Username: ")
for i in range(len(usernames)):
    if input_username in usernames:
        in_usernames = True
    else:
        input_username = False
if in_usernames:
    print("Access granted")
else:
    print('Access denied')