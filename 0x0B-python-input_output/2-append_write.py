#!/usr/bin/python3
"""Task 2 Project 0x0B Python"""


def append_write(filename="", text=""):
    """"Function that open a file to append content"""
    with open(filename, "a", encoding="utf-8") as f:
        w = f.write(text)
    return w
