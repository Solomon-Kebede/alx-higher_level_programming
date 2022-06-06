#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 | idx > len(my_list):
        return my_list
    else:
        new_list = my_list[:idx]
        for i in my_list[idx + 1:]:
            new_list.append(i)
        my_list = new_list
        return my_list
