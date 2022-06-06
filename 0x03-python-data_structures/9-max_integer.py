#!/usr/bin/python3

def max_integer(my_list=[]):
    len_list = len(my_list)
    if len_list == 0:
        return None
    elif len_list > 0:
        maximum = my_list[0]
        for i in range(len_list):
            if my_list[i] > maximum:
                maximum = my_list[i]
        return maximum
