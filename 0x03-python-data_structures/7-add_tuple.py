#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    result, list_a, list_b = list(), list(), list()
    count = 0
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    for i in range(len_a):
        list_a.append(tuple_a[i])
        count += 1
    for i in range(2 - count):
        list_a.append(0)

    count = 0
    for j in range(len_b):
        list_b.append(tuple_b[j])
        count += 1
    for j in range(2 - count):
        list_b.append(0)

    for i in range(2):
        result.append(list_a[i] + list_b[i])
    return tuple(result)
