#!/usr/bin/python3
"""Task 8 Project 0x0B Python"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    dictionary = obj.__dict__
    return dictionary
