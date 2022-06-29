#!/usr/bin/python3
"""A class rectangle that defines a rectangle"""

class Rectangle :
    """A rectangle
    
    Attributes:
        __width (int): width of the rectangle

    """

    def __init__(self, width = 0, height = 0):
        """Initializes the rectangle

        Args:
            width (int): width of the horizontal side of the rectangle
            height (int): height of the vertical side of the rectangle

        Returns: None

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter of width

        Returns:
            The width of the rectangle

        """

        return self.__width

    @width.setter
    def width(self, value):
        """setter of __width

        Args:
            value (int): the width of the rectangle

        Returns:
            None

        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    @property
    def height(self):
        """getter of __height

        Returns:
            The height of the rectangle

        """

        return self.height

    @height.setter
    def height(self, value):
        """setter of __height

        Args:
            value (int): the height of the rectangle

        Returns:
            None

        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
