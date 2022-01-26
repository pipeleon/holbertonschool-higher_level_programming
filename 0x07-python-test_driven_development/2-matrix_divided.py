#!/usr/bin/python3
"""Task 2 Project 0x07 Python"""


def matrix_divided(matrix, div):
    """Funtion to divide each element of a matrix"""
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError(err1)

    for i in range(len(matrix)):
        if i + 1 < len(matrix):
            if len(matrix[i]) is not len(matrix[i + 1]):
                raise TypeError(err2)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = []
    for i in range(len(matrix)):
        new2 = []
        for j in range(len(matrix[i])):
            new2.append(round((matrix[i][j] / div), 2))
        new.append(new2)
    return new
