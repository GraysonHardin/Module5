"""
Program: debugging_example.py
Author: Grayson Hardin
Last date modified: 9/22/2020

This file corrects the error where the function was only outputting 1-4 when it should have been outputting 1-5.
On line 13, it used to be, "for counter in range(1, number)" which had to be corrected to, "for counter in range(1, number + 1)

"""


def print_to_number(number):
    for counter in range(1, number + 1):  # The issue is that '1' is the starting position which has a value of '0' Therefore, the loop will output: 0, 1, 2, 3, 4. In order to fix, simply modify line 13 to, "(1, number + 1):"
        print(counter)


if __name__ == '__main__':
    print_to_number(5)
