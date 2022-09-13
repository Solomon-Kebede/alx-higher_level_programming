#!/usr/bin/python3
"""Module Documentation"""


def say_my_name(first_name, last_name=""):
    """ prints concatenated name """
    if isinstance(first_name, str) and isinstance(last_name, str):
        print(f"My name is {first_name} {last_name}")
    elif not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
