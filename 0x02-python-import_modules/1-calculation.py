#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import add, sub, mul, div
    suma = add(a, b)
    print("{} + {} = {}".format(a, b, suma))
    resta = sub(a, b)
    print("{} + {} = {}".format(a, b, resta))
    mult = mul(a, b)
    print("{} + {} = {}".format(a, b, mult))
    divs = div(a, b)
    print("{} + {} = {}".format(a, b, divs))
