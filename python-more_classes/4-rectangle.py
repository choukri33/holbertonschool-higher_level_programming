#!/usr/bin/python3

"""Defines a Rectangle class with various utility methods."""


class Rectangle:
    """A class that defines a rectangle by its width and height."""
    
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance with optional width and height.
        
        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle, ensuring it is a non-negative integer.
        
        Args:
            value (int): The new width value.
        
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle, ensuring it is a non-negative integer.
        
        Args:
            value (int): The new height value.
        
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle.
        
        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of the rectangle.
        
        Returns:
            int: The perimeter of the rectangle, or 0 if either width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle using the `#` character.
        
        Returns:
            str: A string representing the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        
        rectangle = []
        for _ in range(self.__height):
            rectangle.append("#" * self.__width)
        return "\n".join(rectangle)

    def __repr__(self):
        """Returns a string representation of the rectangle instance.
        
        Returns:
            str: A string that can be used to recreate the rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"
