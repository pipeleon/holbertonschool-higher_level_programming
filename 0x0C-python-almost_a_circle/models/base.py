#!/usr/bin/python3
"""Task 1 Project 0x0C Python"""


class Base():
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
