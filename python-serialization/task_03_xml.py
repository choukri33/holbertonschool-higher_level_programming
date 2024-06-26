#!/usr/bin/env python3
""" Module
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize to xml file"""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Load from xml and deserialize"""
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary