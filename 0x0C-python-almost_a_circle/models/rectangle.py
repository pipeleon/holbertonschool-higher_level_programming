#!/usr/bin/python3
"""Rectangle Module - Project 0x0C Python"""
from .base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Function to create a new instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width Method when called"""
        return self.__width

    @property
    def height(self):
        """Height Method when called"""
        return self.__height

    @property
    def x(self):
        """X Method when called"""
        return self.__x

    @property
    def y(self):
        """Y Method when called"""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Method of calculation of Area"""
        return self.__width * self.__height

    def display(self):
        """Method to print the Rectangle"""
        string_r = ""
        for i in range(self.__y):
            string_r += "\n"
        for i in range(self.__height):
            for j in range(self.__x):
                string_r += " "
            for j in range(self.__width):
                string_r += "#"
            if i != self.__height - 1:
                string_r += "\n"
        print(string_r)

    def __str__(self):
        """Method for the string representation"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Method to update an atributte by each argument passed"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Dict represantation"""
        new = {}
        new["id"] = self.id
        new["width"] = self.__width
        new["height"] = self.__height
        new["x"] = self.__x
        new["y"] = self.__y
        return new

    def update_list(self, list):
        """Update by List"""
        if list:
            self.id = int(list[0])
            self.__width = int(list[1])
            self.__height = int(list[2])
            self.__x = int(list[3])
            self.__y = int(list[4])

    def to_list(self):
        """Atributtes to List"""
        new = []
        new.append(self.id)
        new.append(self.__width)
        new.append(self.__height)
        new.append(self.__x)
        new.append(self.__y)
        return new
