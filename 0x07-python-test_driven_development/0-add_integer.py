#!/usr/bin/python3
"""Task 0 Project 0x07 Python"""


def add_integer(a, b=98):
    """Function to add two Integers or Floats"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
