#!/usr/bin/python3
"""
returns True if the object is an instance of a class that inherited (directly or indirectly)
from the specified class ; otherwise False.
"""

def inherits_from(obj, a_class):
    """
    Args:
        obj: object
        a_class: type to check against
        Boolean: boolean
    """
    
    return type(obj) != a_class and issubclass(type(obj), a_class)