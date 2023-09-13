#!/usr/bin/python3

"""A method that defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """ A method that represent Pascal's Triangle
    Returns:
        a list of integer
    """
    if n <= 0:
        return[]

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
