#!/usr/bin/python3
"""write a class student"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        """initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """creates a dict"""
        if (type(attrs) == list and
                all(type(e) == str for e in attrs)):
            return {i: getattr(self,i) for i in attrs if hasattr(self, i)}
        return self.__dict__