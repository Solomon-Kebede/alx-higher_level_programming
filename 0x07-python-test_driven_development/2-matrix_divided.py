#!/usr/bin/python3
"""Module Documentation"""


def matrix_divided(matrix, div):
    """ Divides Matrix by divider """
    error_1 = 'matrix must be a matrix (list of lists) of integers/floats'
    error_2 = 'Each row of the matrix must have the same size'
    error_3 = 'div must be a number'
    error_4 = 'division by zero'
    if not isinstance(matrix, list):
        raise TypeError(error_1)
    elif isinstance(matrix, list):
        list_length_init = len(matrix[0])
        for i in range(len(matrix)):
            if not isinstance(matrix[i], list):
                raise TypeError(error_1)
            else:
                if len(matrix[i]) != list_length_init:
                    raise TypeError(error_2)
                for j in matrix[i]:
                    if not isinstance(j, int) and not isinstance(j, float):
                        raise TypeError(error_1)
                        # print('What is', type(j))
                    elif isinstance(j, int) or isinstance(j, float):
                        # print(j)
                        pass
    if not isinstance(div, int) or not isinstance(div, int):
        raise TypeError(error_3)
    if div == 0:
        raise ZeroDivisionError(error_4)
    lso = list()
    for i in range(len(matrix)):
        lsi = list()
        for j in matrix[i]:
            lsi.append(round((j/div), 2))
        lso.append(lsi)
    return lso

