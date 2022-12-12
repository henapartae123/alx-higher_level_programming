#!/usr/bin/python3
"""writes an object to a text file, using a json representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes a json"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(json.dumps(my_obj))
