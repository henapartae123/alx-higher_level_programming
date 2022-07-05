#!/usr/bin/python3
"""returns the dictionary description with simple data 
structure (list, dictionary, string, integer and boolean) 
for json serialization of an object
"""


def class_to_json(obj):
    """returns a dict """
    return obj.__dict__
    