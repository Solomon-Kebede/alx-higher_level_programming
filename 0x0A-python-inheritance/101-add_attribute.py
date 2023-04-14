#!/usr/bin/python3
'''
Write a function that adds a new attribute to an object if it’s possible:
    - Raise a `TypeError` exception, with the message
    `can't add new attribute` if the object can’t have new attribute
    - You are not allowed to use `try/except`
    - You are not allowed to import any module
'''


def add_attribute(mc, name: str, value: str):
    ''' adds a new attribute to an object
    if it’s possible'''
    if '__dict__' in mc.__dir__():
        mc.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
