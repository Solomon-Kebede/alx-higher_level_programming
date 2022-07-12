#!/usr/bin/python3
"""Module level comment"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class documentation"""
    def __init__(self, size, x=0, y=0, id=None):
        '''Function documentation'''
        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    @property
    def size(self):
        """size getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter method"""
        if isinstance(value, int) and value > 0:
            self.__size = value
        elif not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

    def __str__(self):
        """override the method to display rectangle info"""
        x = self.x
        y = self.y
        return f"[Square] ({self.id}) {x}/{y} - {self.size}"
