#!/usr/bin/python3
"""Task 4 0x11. Python - Network #1"""
import requests


if __name__ == "__main__":
    """Main Function"""
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(r.text))
    print("\t- content:", r.text)
