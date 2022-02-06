#!/usr/bin/python3
"""Task 1 Project 0x0C Python"""
import json


class Base():
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            new = []
            for i in list_objs:
                new.append(i.to_dictionary())
            f.write(Base.to_json_string(new))
