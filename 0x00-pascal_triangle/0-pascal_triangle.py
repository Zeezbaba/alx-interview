#!/usr/bin/python3
"""A function that that returns a list of lists of
integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = []

    # return (trianlgle if n <= 0)
    if n <= 0:
        return triangle
    for i in range(n):
        row = []

        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)
    return triangle
