#!/usr/bin/python3

'''
Write a class `MyInt` that inherits from `int`:
    - `MyInt` is a rebel. `MyInt` has `==` and `!=` operators inverted
    - You are not allowed to import any module
'''


class MyInt(int):
    '''Overriding base integer class'''
    def __eq__(self, other):
        '''when equals not equal'''
        return str(self) != str(other)

    def __ne__(self, other):
        '''when not equal, equal'''
        return str(self) == str(other)
