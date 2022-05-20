#!/usr/bin/python3
"""Task 10 0x11. Python - Network #1"""
import requests
import sys


if __name__ == "__main__":
    """Main Function"""
    r = requests.get("https://api.github.com/user", auth=(sys.argv[1], sys.argv[2]))

    print(r.json().get('id'))
