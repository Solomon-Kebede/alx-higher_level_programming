#!/usr/bin/python3

'''
-Write a class `Rectangle` that inherits
from `BaseGeometry` (`7-base_geometry.py`).
    -Instantiation with `width` and `height`:
    `def __init__(self, width, height):`
        -`width` and `height` must be private. No getter or setter
        -`width` and `height` must be positive integers, validated
        by `integer_validator`
'''


class Rectangle(BaseGeometry):
    '''Rectangle class'''
    def __init__(self, width, height):
        '''Initialize width and height'''
        if super().integer_validator("width", width) is None:
            self.__width = width
        if super().integer_validator("height", height) is None:
            self.__height = height
