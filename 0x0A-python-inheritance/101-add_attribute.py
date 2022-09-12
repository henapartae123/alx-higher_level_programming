#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible

    Args:
        obj (any): The object to add an attribute to
        att (str): The name of the attribute to add to the object
        value (any): The value of the attribute

    Raises:
        TypeError:  if the object cannot have new attribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
