#!/usr/bin/python3
"""Task 5 0x11. Python - Network #1"""
import requests
import sys


if __name__ == "__main__":
    """Main Function"""
    params ={}
    params['email'] = sys.argv[2]
    r = requests.post(sys.argv[1], data=params)
    print(r.text)
