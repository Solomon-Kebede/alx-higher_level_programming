#!/usr/bin/python3

'''
-Write a function that returns the list of available
attributes and methods of an object:
    -Prototype: `def lookup(obj)`:
    -Returns a `list` object
'''


def lookup(obj):
    '''Returns the list of available attributes and methods'''
    return dir(obj)
