#!/usr/bin/python3
"""
Module matrix_divided
Divides each element of a matrix of numbers by a number
Returns a new matrix
"""

def matrix_divided(matrix, div):
    """
    Returns a new matrix (list of lists)
    with the result of the division of matrix by div
    rounded to 2 decimal places.
    """

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix

