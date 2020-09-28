""""
Program: loop.py
Author: Grayson Hardin
Last date modified: 9/28/2020

Program contains a basic list that can be looped once or multiple times. Additionally, there is a second loop (x) that can print the numbers starting from 99 and end at 33.

"""

number_list = [1, 2, 3, 4, 5]

for i in range(1):  # Runs the loop once.
    print(number_list)

for x in range(99, 31, -2):  # Note: the end is technically "33" when ran. If changed to 33 in the code, it will end the loop at 35.
    print(x)
