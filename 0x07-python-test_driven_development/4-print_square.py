#!/usr/bin/python3
# 4-print_square.py
"""Defines a square-printing function."""


def print_square(size):
    """Print a square with the # character.
    Args:
        size (int): The dimension of the square.

    Raises:
        TypeError: size must be an integer.
        ValueError: size must be >= 0

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
