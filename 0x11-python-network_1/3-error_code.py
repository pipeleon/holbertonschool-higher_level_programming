#!/usr/bin/python3
"""Task 3 0x11. Python - Network #1"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    """Main Function"""
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try: 
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
