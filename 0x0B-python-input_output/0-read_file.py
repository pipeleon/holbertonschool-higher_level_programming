#!/usr/bin/python3
"""Task 0 Project 0x0B Python"""


def read_file(filename=""):
    """"Function that openand read a file to print its content"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
