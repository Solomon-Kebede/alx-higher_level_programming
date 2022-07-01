#!/usr/bin/python3
"""Module Documentation"""


def matrix_divided(matrix, div):
    """ Divides Matrix by divider """
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists)\
         of integers/floats')
    elif isinstance(matrix, list):
        list_length_init = len(matrix[0])
        for i in range(len(matrix)):
            if not isinstance(matrix[i], list):
                raise TypeError('matrix must be a matrix (list of lists)\
                 of integers/floats')
            else:
                if len(matrix[i]) != list_length_init:
                    raise TypeError('Each row of the matrix must \
                        have the same size')
    if not isinstance(div, int) or not isinstance(div, int):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    lso = list()
    for i in range(len(matrix)):
        lsi = list()
        for j in matrix[i]:
            lsi.append(round((j/div), 2))
        lso.append(lsi)
    return lso
