#!/usr/bin/python3
"""creates an object from a json file"""
import json


def load_from_json_file(filename):
    """writes an object"""
    
    with open(filename) as myFile:
        return json.load(myFile)
