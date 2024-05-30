#!/usr/bin/python3
"""function append in file"""


def append_write(filename="", text=""):
    """function that appends a string to the end of a file (UTF8)
    and returns the added number: """
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(text)
    return len(text)
