#!/usr/bin/python3
def no_c(my_string):
    new = []
    for i in my_string:
        if not (i == "c" or i == "C"):
            new.append(i)
    convert = ""
    for i in new:
        convert += i
    return convert
