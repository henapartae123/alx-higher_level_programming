#!/usr/bin/python3
"""
returns True if the object is an instance of, or if the object is
an instance of a class that inherited from, the specified
class; otherwise False.
"""

def is_kind_of_class(obj, a_class):
    """

    Args:
        obj (Any): object to check
        a_class (type): type to check against
    
    Returns:
        boolean: boolean
    """
    return isinstance(obj, a_class)
    