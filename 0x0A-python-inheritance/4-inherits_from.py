#!/usr/bin/python3
"""Task 4 Project 0x0A Python"""


def inherits_from(obj, a_class):
    """Compares if and obj is an instance of a class that inherited"""
    if obj.__class__ is a_class:
        return False
    return issubclass(obj.__class__, a_class)
