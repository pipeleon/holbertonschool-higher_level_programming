#!/usr/bin/python3
"""Task 1 Project 0x0B Python"""


def write_file(filename="", text=""):
    """"Function that open a file to write content"""
    with open(filename, "w", encoding="utf-8") as f:
        w = f.write(text)
    return w
