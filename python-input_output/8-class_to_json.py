#!/usr/bin/python3
"""Function to get the dictionary representation of an object's
attributes for JSON serialization"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structures
    (list, dictionary, string, integer, and boolean)
    for JSON serialization of an object.

    Args:
        obj: The object to serialize.

    Returns:
        dict: The dictionary representation of the object's attributes.
    """
    return obj.__dict__
