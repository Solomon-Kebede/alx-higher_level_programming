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
        if isinstance(value, int) and value > 0:
            self.__width = value
        elif not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

    @height.setter
    def height(self, value):
        """height getter method"""
        if isinstance(value, int) and value > 0:
            self.__height = value
        elif not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

    @x.setter
    def x(self, value):
        """x setter method"""
        if isinstance(value, int) and value >= 0:
            self.__x = value
        elif not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value <= 0:
            raise ValueError("x must be >= 0")

    @y.setter
    def y(self, value):
        """y setter method"""
        if isinstance(value, int) and value >= 0:
            self.__y = value
        elif not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value <= 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """calculate the area of a rectangle"""
        return (self.width * self.height)

    def display(self):
        """print rectangle"""
        line = '#' * self.width
        print(((line + '\n') * (self.height - 1)) + line)

    def __str__(self):
        """override the method to display rectangle info"""
        return f"[Rectangle] \
                ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
