#!/usr/bin/python3
"""Defines a class named BaseGeometry."""


class BaseGeometry:
    """Represents a base geometry class."""

    def area(self):
        """Raises an Exception with a message."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value to be an integer and greater than 0.

        Args:
            name (str): The name associated with the value.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

