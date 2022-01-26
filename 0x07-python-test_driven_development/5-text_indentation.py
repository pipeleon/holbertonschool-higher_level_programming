#!/usr/bin/python3
"""Task 5 Project 0x07 Python"""


def text_indentation(text):
    """Prints a text slitting it by . : ?"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in [".", ":", "?"]:
            print(text[i])
            print("")
            i += 1
        else:
            print(text[i], end="")
        i += 1
