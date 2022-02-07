#!/usr/bin/python3
"""Project 0x0C Python"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Setter size"""
        self.width = value
        self.height = value
        self.__size = value

    def __str__(self):
        """Method for the string representation"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.__size)

    def update(self, *args, **kwargs):
        """Method to update an atributte by each argument passed"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        new = {}
        new["id"] = self.id
        new["size"] = self.__size
        new["x"] = self.x
        new["y"] = self.y
        return new

    def update_list(self, list):
        if list:
            self.id = int(list[0])
            self.size = int(list[1])
            self.x = int(list[2])
            self.y = int(list[3])

    def to_list(self):
        new = []
        new.append(self.id)
        new.append(self.__size)
        new.append(self.x)
        new.append(self.y)
        return new
