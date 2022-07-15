#!/usr/bin/python3
"""Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init the Square"""

        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        """Get the size of the Square"""

        return self.width

    @size.setter
    def size(self, value):
        """set the size of the Square"""

        self.width = value
        self.height = value