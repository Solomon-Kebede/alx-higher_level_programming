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


class BaseGeometry(BaseException):
    '''Class for BaseGeometry'''
    def area(self):
        '''Area method'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Integer validator'''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    '''Rectangle class'''
    def __init__(self, width, height):
        '''Initialize width and height'''
        if super().integer_validator("width", width) is None:
            self.__width = width
        if super().integer_validator("height", height) is None:
            self.__height = height
