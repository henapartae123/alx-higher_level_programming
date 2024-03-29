#!/usr/bin/python3
'''Rectangle class module'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''init rectangle'''

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''get width of the rectangle'''

        return self.__width

    @width.setter
    def width(self, value):
        '''set width of the rectangle'''

        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''get height of the rectangle'''

        return self.__height

    @height.setter
    def height(self, value):
        '''set height of the rectangle'''

        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''get x of the rectangle'''

        return self.__x

    @x.setter
    def x(self, value):
        '''set x of the rectangle'''

        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        '''get y of the rectangle'''

        return self.__y

    @y.setter
    def y(self, value):
        '''set y of a rectangle'''

        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, isequal=True):
        '''check the value as int and >= 0'''

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if isequal and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not isequal and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        '''area of the rectangle'''

        return self.width * self.height

    def display(self):
        '''print stdout of the rectangle'''

        display = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(display, end='')

    def __str__(self):
        '''str info about a rectangle'''
        return '[Rectangle] ({}) {}/{} - {}/{}'. \
            format(self.id, self.x, self.y, self.width, self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''update instance attributes via */**args'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''update instance attributes via */** args'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''dictionary representation of the class'''

        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
