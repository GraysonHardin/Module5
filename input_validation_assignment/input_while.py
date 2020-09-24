"""
Program: input_while.py
Author: Grayson Hardin
Last date modified: 9/24/2020

The program will take multiple inputs and store it within a list if it is within the parameters (1-100).
I have ran this program many times and have provided my documentation down below.

"""

stopping_value = 1000
user_list = []
user_input = int(input('Enter a number (1-100) or enter 1000 to exit: '))
while user_input != stopping_value:  # This while loop will function until the stopping_value is met.
    while user_input > 100 or user_input < 1:  # Here, the conditions are made. In order for a number to be added, it has to be within the range. In addition, the loop cannot be ended while outside of the range (1-100).
        user_input = int(input('Value is outside of the range. Try again: '))  # Prompting user for another input.
    user_list.append(user_input)  # If input is within the range of 1-100, it will be added to the list.
    user_input = int(input('Enter another number: '))  # loop continues...

for x in user_list:  # this will print the value of user_list. I've set this up so it only prints after the program changes, but this can be changed by tabbing it in.
    print(x)
