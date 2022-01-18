#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        n = fct(args[0], args[1])
        return n
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
        return None
