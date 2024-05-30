#!/usr/bin/python3
"""Function that writes a string to a text file (UTF8) and
    returns the number of characters written"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as f:
        """Write string and count characters"""

        chars_written = f.write(text)
        return len(text)
