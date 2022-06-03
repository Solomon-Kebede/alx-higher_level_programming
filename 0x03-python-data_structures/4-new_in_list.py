#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    else:
        length = len(my_list)
        if idx > length:
            return my_list
        else:
            new_list = list()
            for i in range(length):
                new_list.append(my_list[i])
            my_list[idx] = element
            return new_list
