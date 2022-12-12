#!/usr/bin/python3
"""returns a list of lists of integers representing 
the Pascal triangle of n
"""


def pascal_triangle(n):
    """Returns a  triangle"""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        triangles = triangle[-1]
        tmp = [1]
        for i in range(len(triangles) - 1):
            tmp.append(triangles[i] + triangles[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle