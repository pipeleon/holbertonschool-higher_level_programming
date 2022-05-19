#!/usr/bin/python3
"""Task 5 0x11. Python - Network #1"""
import requests
import sys


if __name__ == "__main__":
    """Main Function"""
    r = requests.get(sys.argv[1])
    if r.status_code == 200:
        print(r.text)
    else:
        print("Error code:", r.status_code)
