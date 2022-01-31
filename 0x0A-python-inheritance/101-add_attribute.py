#!/usr/bin/python3
"""Task 101 Project 0x0A Python"""


def add_attribute(object, atribute, value):
    """Fucntion that set an atributte if it is posible"""
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(object, atribute, value)    
