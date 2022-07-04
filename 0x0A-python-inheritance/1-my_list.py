#!/usr/bin/python3
"""
Returns a list object
"""

class MyList(list):
    """Custom List
    """
    def print_sorted(self):
        """
        Returns: 
            prints the list, but sorted (ascending sort)
            
        """
        print(sorted(self))