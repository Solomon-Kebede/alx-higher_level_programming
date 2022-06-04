#!/usr/bin/python3

def no_c(my_string):
    new = list()
    for i in my_string:
        if i in 'cC':
            continue
        else:
            new.append(i)
    return ("".join(new))
