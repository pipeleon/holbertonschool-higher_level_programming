#!/usr/bin/python3
"""Task 7 Project 0x0B Python"""
import sys
import os.path

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if __name__ == "__main__":
    if not os.path.exists("add_item.json"):
        new = []
        for i in range(1, len(sys.argv)):
            new.append(sys.argv[i])
        save_to_json_file(new, "add_item.json")
    else:
        new = load_from_json_file("add_item.json")
        for i in range(1, len(sys.argv)):
            new.append(sys.argv[i])
        save_to_json_file(new, "add_item.json")
