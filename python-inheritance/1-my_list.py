#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """class from list"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
