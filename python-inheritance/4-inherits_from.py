#!/usr/bin/python3
"""Defines a function to check if an object is an instance of a class
that inherits from the specified class"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of a class that inherited
    from a_class

    Args:
        obj: object to check
        a_class: class to compare to

    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class; otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
