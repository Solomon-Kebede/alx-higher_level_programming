#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    r = list()
    for k in range(len(matrix)):
        r.append(list(tuple(matrix[k])))
    for i in r:
        for j in i:
            r[r.index(i)][i.index(j)] = matrix[r.index(i)][i.index(j)] ** 2
    return r
