#!/usr/bin/python3
"""
Module matrix_mul
Multiplies two matrices and returns the result.
"""

def validate_matrix(matrix, matrix_name):
    """Validate a matrix."""
    if not isinstance(matrix, list):
        raise TypeError(f"{matrix_name} must be a list")
    
    if not matrix or any(not isinstance(row, list) or not row for row in matrix):
        raise ValueError(f"{matrix_name} can't be empty or contain empty rows")
    
    num_cols = len(matrix[0])
    if not all(len(row) == num_cols for row in matrix):
        raise TypeError(f"Each row of {matrix_name} must have the same size")

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(f"{matrix_name} should contain only integers or floats")

def matrix_mul(m_a, m_b):
    """
    Return the matrix resulting from
    the multiplication of m_a and m_b.
    """

    validate_matrix(m_a, "m_a")
    validate_matrix(m_b, "m_b")

    num_cols_m_a = len(m_a[0])
    num_rows_m_b = len(m_b)

    if num_cols_m_a != num_rows_m_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

