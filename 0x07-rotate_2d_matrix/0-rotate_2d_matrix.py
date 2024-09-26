#!/usr/bin/python3
"""rotate 2D matrix and 90 degrees in-place"""

def rotate_2d_matrix(matrix):
    """rotating a 2D matrix
    Args:
        matrix: List of lists of numbers
    Return:
        return nothing
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
