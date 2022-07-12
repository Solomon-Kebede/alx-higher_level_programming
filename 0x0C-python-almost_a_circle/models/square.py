#!/usr/bin/python3
"""Module level comment"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class documentation"""
    def __init__(self, size, x=0, y=0, id=None):
        '''Function documentation'''
        super().__init__(size, size, x, y, id)
