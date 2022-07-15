#!/usr/bin/python3
'''Base class module'''
from json import dumps
from json import loads

class Base:
    '''Base class'''

    __nb_objects = 0

    def __init__(self, id=None):

        '''init magic'''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''json representation of the list of dictionaries'''

        if list_dictionaries is None:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''retrieve __dict__ from json'''
        if json_string is None:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes json representation of list of objects to a file'''

        filename = cls.__name__ + ".json"
        text = []
        if list_objs is not None:
            for lst in list_objs:
                text.append(lst.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as f:
            return f.write(Base.to_json_string(text))

    @classmethod
    def create(cls, **dictionary):
        """create an instance with all attributes"""

        from models.rectangle import Rectangle
        from models.square import Square
        
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new