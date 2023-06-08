#!/usr/bin/python3
"""
A function that rotates a n x n @D matrix 90 degress clockwise in-place
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise
    Args:
        matrix (list): 2D square matrix
    Return:
        None
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp

    for i in range(n):
        for j in range(int(n / 2)):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = tmp
