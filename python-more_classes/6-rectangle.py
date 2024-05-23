#!/usr/bin/python3


"""create class 'rectangle'"""


class Rectangle:
    """class rectangle"""

    """public class attribute"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """private instantiation"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    """decorators for width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """decorators for height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """return an informal string version of the object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        return ('\n'.join('#' * self.__width for i in range(self.__height)))

    def __repr__(self):
        """return an official string version of the objetc"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """print message when delete an object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1