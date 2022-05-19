#!/usr/bin/python3
"""Task 2 0x11. Python - Network #1"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    """Main Function"""
    url = sys.argv[1]
    data = {}
    data['email'] = sys.argv[2]
    url_values = urllib.parse.urlencode(data).encode('ascii')
    req = urllib.request.Request(url, url_values)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf8'))
