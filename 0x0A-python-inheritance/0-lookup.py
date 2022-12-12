#!/usr/bin/python3
"""
Returns the list of available attributes and methods of an object:
"""


def lookup(obj):
    """Returns a list object.

    Args:
        obj : object

    Returns:
        list: list of attributes and members

    """
    return dir(obj)
