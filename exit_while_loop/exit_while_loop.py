"""
Program: exit_while_loop.py
Author: Grayson Hardin
Last date modified: 9/24/2020

This program is essentially the same as input_while.py, but with added features. It provides more 'break' scenarios if the user wishes to end the loop.
"""
stopping_value = 1000
user_list = []
user_input = int(input("Enter a number between 1 and 100. To end, enter 1000. "))
while user_input != stopping_value:
    while user_input > 100 or user_input < 1:  # Loop conditions
        user_input = int(input("Value is outside of the range. Try again: "))
        if user_input == stopping_value:  # Loop will end if it = 1000
            break
    if user_input == stopping_value:  # Loop will end if it = 1000
        break
    user_list.append(user_input)   # Adds the user input to the list (assuming it is within the loop conditions)
    user_input = int(input("Enter a number: "))
print('Output: ')

for x in user_list:  # Prints list
    print(x)
