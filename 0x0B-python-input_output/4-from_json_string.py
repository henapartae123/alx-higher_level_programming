#!/usr/bin/python3
"""returns an object from a json representation"""
import json


def from_json_string(my_str):
    """returns an objects"""

    return json.loads(my_str)
    