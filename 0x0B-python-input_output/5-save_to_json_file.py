#!/usr/bin/python3
"""Task 5 Project 0x0B Python"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
