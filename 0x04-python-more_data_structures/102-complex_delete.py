#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i, j in list(a_dictionary.items()):
        if j is value:
            a_dictionary.pop(i)
    return a_dictionary