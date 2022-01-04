#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = []
    for i in range(2):
        if i < len(tuple_a):
            a = tuple_a[i]
        else:
            a = 0
        if i < len(tuple_b):
            b = tuple_b[i]
        else:
            b = 0
        new.append(a + b) 
    return tuple(new)
