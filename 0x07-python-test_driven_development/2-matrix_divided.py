#!/usr/bin/python3
# 2-matrix_divided.py
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix representing the result of the division.
    """
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    matrix_new = [x[:] for x in matrix]
    for line in matrix_new:
        if len(line) != len(matrix_new[0]):
            raise TypeError('Each row of the matrix must have the same size')

        for element_index, element in enumerate(line):
            if not isinstance(element, (int, float)):
                raise TypeError(
                    'matrix must be a matrix (list of lists)'
                    ' of integers/floats'
                )

            line[element_index] = round(element/div, 2)

    return matrix_new
