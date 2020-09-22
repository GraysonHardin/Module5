"""
Program: debugging_example.py
Author: Grayson Hardin
Last date modified: 9/22/2020

This file corrects the error where the function was only outputting 1-4 when it should have been outputting 1-5.
On line 12, it used to be, "for counter in range(1, number)" which had to be corrected to, "for counter in range(1, number + 1)

"""


def print_to_number(number):
    for counter in range(1, number + 1):
        print(counter)


if __name__ == '__main__':
    print_to_number(5)
