#!/usr/bin/python3
"""Module level comment"""


from models.base import Base


class Rectangle(Base):
    """Class documentation"""
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Function documentation'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @width.setter
    def width(self, value):
        """width setter method"""
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter method"""
        self.__height = value

    @x.setter
    def x(self, value):
        """x setter method"""
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter method"""
        self.__y = value
