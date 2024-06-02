#!/usr/bin/python3
"""write a class Student"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """Public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        """If attrs is a list of strings, only attribute names contained
        in this list must be retrieved."""
        if type(attrs) is list:
            new_dict = {}
            for key in self.__dict__:
                for key2 in attrs:
                    if key == key2:
                        new_dict[key] = self.__dict__[key]
            return new_dict
        return (self.__dict__)
