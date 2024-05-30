#!/usr/bin/python3
"""Module containing a function to read and print a file"""

def read_file(filename=""):
    """Reads a text file (UTF8) and prints its content to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content, end="")

