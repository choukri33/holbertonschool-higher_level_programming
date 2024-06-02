#!/usr/bin/python3
"""functions for load_from_json_file"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, 'r') as file:
        json_data = file.read()
        obj = json.loads(json_data)
        return obj
