#!/usr/bin/python3
"""script that adds all arguments to
a Python list, and then save them to a file"""
import json
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    """loads list from add_item.json"""
    arglist = load_from_json_file("add_item.json")
except FileNotFoundError:
    """if the list is not found, it is created empty"""
    arglist = []

"""adds arguments starting from the 2nd arg (the 1st is the file name)."""
arglist += argv[1:]
"""saves the list in the specified file"""
save_to_json_file(arglist, "add_item.json")