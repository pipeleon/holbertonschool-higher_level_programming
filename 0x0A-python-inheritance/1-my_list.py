#!/usr/bin/python3
"""Task 1 Project 0x0A Python"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        new = MyList()
        for i in self:
            new.append(i)
        new.sort()
        print(new)
