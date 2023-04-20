#!/usr/bin/python3
"""Creating a Pascal triangle of any number"""


def pascal_triangle(n):
    """
    Returns a lists of lists of integers representing the Pascal triangle of n
    """
    triangle = []

    # check if n is less than or equals to 0
    if n <= 0:
        return triangle

    for i in range(n):
        tmp = []

        for j in range(i+1):
            if j == 0 or j == i:
                tmp.append(1)
            else:
                tmp.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(tmp)

    return triangle
