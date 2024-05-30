#!/usr/bin/python3
"""module json"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.

    Args:
        my_obj: The object to be serialized to JSON.
        filename (str): The name of the file to save the JSON data.

    Returns:
        None
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
