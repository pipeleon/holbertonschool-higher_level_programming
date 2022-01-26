#!/usr/bin/python3
"""Task 3 Project 0x07 Python"""


def say_my_name(first_name, last_name=""):
    """Funtion to print the name given"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
