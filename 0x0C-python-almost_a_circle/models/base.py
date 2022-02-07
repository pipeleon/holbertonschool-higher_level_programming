#!/usr/bin/python3
"""Task 1 Project 0x0C Python"""
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        new = []
        if json_string is None or json_string == "":
            return new
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        new = []
        with open("{}.json".format(cls.__name__), "r", encoding="utf-8") as f:
            if f:
                attr = cls.from_json_string(f.read())
                for i in attr:
                    new.append(cls.create(**i))
                return new
            else:
                return new

    @classmethod
    def save_to_file_csv(cls, list_objs):
        with open("{}.csv".format(cls.__name__), "w", encoding="utf-8") as f:
            new = []
            for i in list_objs:
                new.append(i.to_list())
            w = csv.writer(f)
            w.writerows(new)

    @classmethod
    def create_csv(cls, list):
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update_list(list)
        return new

    @classmethod
    def load_from_file_csv(cls):
        new = []
        with open("{}.csv".format(cls.__name__), "r", encoding="utf-8") as f:
            if f:
                attr = csv.reader(f)
                for i in attr:
                    new.append(cls.create_csv(i))
                return new
            else:
                return new
