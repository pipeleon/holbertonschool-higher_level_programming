#!/usr/bin/python3
def uppercase(str):
    upperc = ""
    for i in range(len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            upperc += chr(ord(str[i]) - 32)
        else:
            upperc += str[i]
    print("{}".format(upperc))
