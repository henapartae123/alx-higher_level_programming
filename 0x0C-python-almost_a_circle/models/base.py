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