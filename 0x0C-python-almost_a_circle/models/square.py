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

    def update(self, *args, **kwargs):
        """override and /updates/assigns an argument to each attribute"""
        order_extern = ['id', 'size', 'x', 'y']
        order_in_class = [
                'id',
                '_Square__size',
                '_Rectangle__x',
                '_Rectangle__y'
                ]
        tmp = dict()
        for i, j, h in zip(order_in_class, args, order_extern):
            tmp[h] = j
            self.__dict__[i] = j
        for k, v in kwargs.items():
            if k not in tmp.keys():
                tmp[k] = v
                if k == 'id':
                    self.__dict__[k] = v
                elif k == 'size':
                    self.__dict__[f"_Square__{k}"] = v
                    self.__dict__[f"_Rectangle__width"] = v
                    self.__dict__[f"_Rectangle__height"] = v
                elif k in order_extern:
                    self.__dict__[f"_Rectangle__{k}"] = v
