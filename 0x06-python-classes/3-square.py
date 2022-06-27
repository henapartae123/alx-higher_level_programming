#!/usr/bin/python3
"""A class square that defines a square"""

class Square :
    """A square
    
    Attributes:
        __size (int): size of the square

    """

    def __init__(self, size = 0):
        """Initializes the square

        Args:
            size (int): size of the side of the square

        Returns: None

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """calculates the area of the square
        
        Return: The area of the square

        """
        
        return (self.__size)
                