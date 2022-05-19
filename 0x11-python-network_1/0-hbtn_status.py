#!/usr/bin/python3
"""Task 0 0x11. Python - Network #1"""
import urllib.request


if __name__ == "__main__":
    """Main Function"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode('utf8'))
