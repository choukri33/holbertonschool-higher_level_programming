#!/usr/bin/python3
"""Function to generate Pascal's triangle"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    Pascal's triangle of n.

    Args:
        n (int): The number of levels in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    for x in range(1, n):
        row = [1]
        for y in range(1, x):
            # Each element is the sum of the two elements above it
            row.append(triangle[x-1][y-1] + triangle[x-1][y])
        # End each row with 1
        row.append(1)
        # Append the row to the triangle
        triangle.append(row)

    return triangle
