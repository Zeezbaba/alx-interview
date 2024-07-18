#!/usr/bin/python3
"""module to rotate a 2D matrix
90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """rotate 90 degrees clockwise
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
