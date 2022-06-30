#!/usr/bin/python3
"""A class rectangle that defines a rectangle"""

class Rectangle :
    """A rectangle
    
    Attributes:
        __width (int): width of the rectangle

    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width = 0, height = 0):
        """Initializes the rectangle

        Args:
            width (int): width of the horizontal side of the rectangle
            height (int): height of the vertical side of the rectangle

        Returns: None

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        
        return ((self.__width) + (self.__height)) * 2

    def __str__(self):
        """prints the retangle

        Returns:
            None
        
        """

        str = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                str = str + '#'
            str = str + '\n'
        return str[:-1]

    def __repr__(self):
        """Rerurn string of the rectangle
        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
    
    def __del__(self):
        """Delete instance of the rectangle
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """calculate which is the largest rectangle
        Arguments:
            rect_1 {Rectangle} -- Firts rectangle
            rect_2 {Rectangle} -- second rectangle

        Returns:
            The biggest rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1
    
    @classmethod
    def square(cls, size=0):
        """Create a rectangle with width == height == size

        Returns:
            A new rectangle
        """
        return cls(size, size)