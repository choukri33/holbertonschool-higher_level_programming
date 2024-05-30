#!/usr/bin/python3
def write_file(filename="", text=""):
    """Function that writes a string to a text file (UTF8) and
    returns the number of characters written"""

    with open(filename, 'w', encoding='utf-8') as f:
        """Write string and count characters"""
        chars_written = f.write(text)
        return chars_written
