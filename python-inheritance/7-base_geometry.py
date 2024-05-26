#!/usr/bin/python3
""" file
"""


class BaseGeometry:
    """ Class that defines attributes of a shape """

    def area(self):
        """ Defines the area of the shape """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Receive the value property """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
