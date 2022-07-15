#!/usr/bin/python3
'''Base class module'''
from json import dumps

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
