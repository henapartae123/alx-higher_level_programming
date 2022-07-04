#!/usr/bin/python3
"""
Returns a list object
"""

class MyList(list):

    """a subclass of list"""
    
    def __init__(self):
        """initializes the object"""
        super().__init__()

    """sorted List"""
    def print_sorted(self):
        """
        Returns: 
            prints the list, but sorted (ascending sort)

        """
        print(sorted(self))
