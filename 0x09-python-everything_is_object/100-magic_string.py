#!/usr/bin/python3
"""Task 100 Project 0x09 """


class Magic():
    prt = 0

    @classmethod
    def sum_ptr(cls):
        cls.prt += 1

def magic_string():
    new = Magic()
    new.sum_ptr()

    printable = ""

    for i in range(new.prt):
        printable += "BestSchool"
        if i + 1 < new.prt:
            printable += ", "
