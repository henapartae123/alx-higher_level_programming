#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """writes a file"""

    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
        
    return len(text)
