#!/usr/bin/python3
"""Task 1 Project 0x06 """


class Rectangle():
    """ Class Rectangle with argument size"""
    def __init__(self, width=0, height=0):
        """ Init method """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Width Method when called"""
        return self.__width

    @property
    def height(self):
        """ Height Method when called"""
        return self.__height

    @width.setter
    def width(self, width):
        """ Setter width"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """ Setter height"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
