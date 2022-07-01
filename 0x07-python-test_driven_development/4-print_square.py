#!/usr/bin/python3
"""Module Documentation"""


def print_square(size):
    """ prints square """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    print(f"{'#' * size}\n" * (size - 1) + f"{'#' * size}")
