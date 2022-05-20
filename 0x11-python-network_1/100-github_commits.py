#!/usr/bin/python3
"""Task 10 0x11. Python - Network #1"""
import requests
import sys


if __name__ == "__main__":
    """Main Function"""
    url = "https://api.github.com/repos/{}/{}/commits"
    r = requests.get(url.format(sys.argv[2], sys.argv[1]))

    commits = r.json()
    
    for i in range(10):
        sha = commits[i].get('sha')
        name = commits[i].get('commit').get('author').get('name')
        print("{}: {}".format(sha, name))
