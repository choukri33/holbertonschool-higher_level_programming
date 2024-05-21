#!/usr/bin/python3
"""Defines a function to check if an object
is an instance of a specified class"""


def is_same_class(obj, a_class):
    """Checks if obj is an instance of a_class

    Args:
        obj: object to check
        a_class: class to compare to

    Returns:
        True if obj is an instance of a_class, otherwise False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
