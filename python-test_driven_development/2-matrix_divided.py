#!/usr/bin/python3
"""Function that divides all elements of a matrix."""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix."""
    
    # Check that matrix is a matrix (list of lists) of integers/floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(item, (int, float)) for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check that all rows of matrix have the same size
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check that div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check that div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of matrix by div and round to 2 decimal places
    new_matrix = [[round(item / div, 2) for item in row] for row in matrix]

    return new_matrix
