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

    def area(self):
        """ Method of calculation of Area"""
        return self.__width * self.__height

    def perimeter(self):
        """ Method of calculation of Perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            string_r = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    string_r += "#"
                if i != self.__height - 1:
                    string_r += "\n"
            return string_r

    def __repr__(self):
        string_r = "Rectangle("
        string_r += str(self.__width)
        string_r += ", "
        string_r += str(self.__height)
        string_r += ")"
        return string_r
