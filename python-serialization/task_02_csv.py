#!/usr/bin/env python3
""" Module
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert csv file to json file"""
    try:
        with open(csv_filename, 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        json_data = json.dumps(data)

        with open('data.json', 'w') as json_file:
            json_file.write(json_data)
        return True
    except FileNotFoundError:
        print("Error: File not found.")
        return False