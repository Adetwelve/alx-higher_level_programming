#!/usr/bin/python3
"""Defines funtion - matrix_divided

    Raises:
        TypeError: If matrix is not int or float
        TypeError: If matrix contains row of different sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0
"""


def matrix_divided(matrix, div):
    """Divide all element of a matrix by div

    Args:
        matix (list): A list of lists of ints or floats
        div (int/float): Divides the matrix

    Returns:
        A  copy of new matrix of the result of the division"""

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists)'
                        ' of integers/floats')
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError('matrix must be a matrix (list of lists)'
                            ' of integers/floats')
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists)'
                                ' of integers/floats')
    return list(map(lambda x: list(map(lambda y:
                round(y / div, 2), x)), matrix.copy()))
