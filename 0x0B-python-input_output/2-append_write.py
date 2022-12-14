#!/usr/bin/python3
"""appends a string at the end of a text file 
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """appends a string"""
    with open(filename, mode="a", encoding="utf-8") as myFile:
        myFile.write(text)
        
    return len(text)
    