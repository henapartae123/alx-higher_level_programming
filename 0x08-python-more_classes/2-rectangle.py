#!/usr/bin/python3
"""A class rectangle that defines a rectangle"""


class Rectangle:
    """A rectangle

    Attributes:
        __width (int): width of the rectangle

    """

    def __init__(self, width=0, height=0):
        """Initializes the rectangle

        Args:
            width (int): width of the horizontal side of the rectangle
            height (int): height of the vertical side of the rectangle

        Returns: None

        """
        self.width = width
        self.height = height

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

        return self.__height

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

    def area(self):
        """calculates the area of the rectangle

        Returns: The area of the rectangle

        """

        return ((self.__width) * (self.__height))

    def perimeter(self):
        """calculates the perimeter of the rectangle

        Returns: The perimeter of the rectangle

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width) + (self.__height)) * 2
