#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        cont = 0
        for i in range(x):
            n = type(my_list[i])
            if n == int:
                print("{:d}".format(my_list[i]), end="")
                cont += 1
    finally:
        print("")
        return cont
