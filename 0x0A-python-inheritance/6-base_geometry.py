#!/usr/bin/python3

'''
-Write a class `BaseGeometry` (based on `5-base_geometry.py`).
    -Public instance method: `def area(self):` that raises
    an `Exception` with the message `area() is not implemented`
    -You are not allowed to import any module
'''


class BaseGeometry(BaseException):
    '''Area method'''
    def area(self):
        raise Exception("area() is not implemented")
