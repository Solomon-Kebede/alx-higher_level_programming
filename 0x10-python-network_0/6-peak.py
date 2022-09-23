#!/usr/bin/python3


""" Technical interview preparation:

    You are not allowed to google anything
    Whiteboard first

Write a function that finds a peak in a list of unsorted integers.

    -Prototype: `def find_peak(list_of_integers):`
    -You are not allowed to import any module
    -Your algorithm must have the lowest complexity (hint: you don’t need
     to go through all numbers to find a peak)
    -`6-peak.py` must contain the function
    -`6-peak.txt` must contain the complexity of your
    algorithm: `O(log(n)), O(n), O(nlog(n)) or O(n2)`
    -Note: there may be more than one peak in the list
"""


def find_peak(list_of_integers):
    """ Test function find_peak """
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) > 0:
        i = list_of_integers[0]
        for j in list_of_integers:
            if i < j:
                i = j
            elif i >= j:
                pass
        return i
        # return list(set(list_of_integers))
