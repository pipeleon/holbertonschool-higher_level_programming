#!/usr/bin/python3
"""Task 8 0x11. Python - Network #1"""
import requests
import sys


if __name__ == "__main__":
    """Main Function"""
    if len(sys.argv) > 0:
        q = sys.argv[1]
    else:
        q = ""
    params = {}
    params['q'] = q
    r = requests.post("http://0.0.0.0:5000/search_user", data=params)

    try:
        if len(r.json().keys()) == 0:
            print("No result")
        else:
            print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
    except:
        print("Not a valid JSON")
