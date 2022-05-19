#!/usr/bin/python3
"""Task 1 0x11. Python - Network #1"""
import sys
import urllib.request
with urllib.request.urlopen(sys.argv[1]) as response:
    html = response.info()
    print(html['X-Request-Id'])
