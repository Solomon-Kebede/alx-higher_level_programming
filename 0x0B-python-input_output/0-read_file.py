#!/usr/bin/python3
"""Module to read a file"""


def read_file(filename=""):
    '''Reads a text file and prints contents to stdout'''
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()
    print(content)
