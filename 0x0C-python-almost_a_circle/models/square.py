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

    def update(self, *args, **kwargs):
        """update arguments"""

        if args and len(args) != 0:
            attr = 0
            for arg in args:
                if attr == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif attr == 1:
                    self.size = arg
                elif attr == 2:
                    self.x = arg
                elif attr == 3:
                    self.y = arg
                attr += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """dictionary representation of the class"""

        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
