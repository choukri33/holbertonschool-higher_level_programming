#!/usr/bin/python3


"""returns 2 int"""


def add_integer(a, b=98):
    """a and b must be int or float"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)