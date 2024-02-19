#!/usr/bin/python
"""create class Mylist"""


class MyList(list):
    """class from list"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
