#!/usr/bin/python3
"""Task 2 Project 0x06 Python"""


class Square():
    """ Class Square with argument size"""
    def __init__(self, size=0):
        """ Init method
        Args:
        param1 (size): Size of a Square"""
        if type(size) != int:
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
