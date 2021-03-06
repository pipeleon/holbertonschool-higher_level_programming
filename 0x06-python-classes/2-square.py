#!/usr/bin/python3
"""Task 2 Project 0x06 Python"""


class Square:
    """ Class Square with argument size"""
    pass

    def __init__(self, size=0):
        """ Init method
        Args:
        param1 (size): Size of a Square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
