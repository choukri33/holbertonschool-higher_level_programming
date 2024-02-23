#!/usr/bin/python3
"""create class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return the rectangle description"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)

    """decorator for size"""
    @property
    def size(self):
        return self.width

    """setter for size"""
    @size.setter
    def size(self, value):
        self.validator(width=value)
        self.validator(height=value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and len(args) > 0:
            list = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, list[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
