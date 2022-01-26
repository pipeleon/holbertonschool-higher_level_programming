#!/usr/bin/python3
"""Task 4 Project 0x07 Python"""


def print_square(size):
    """Function that prints a square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")

    if size == 1:
        print("#")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
