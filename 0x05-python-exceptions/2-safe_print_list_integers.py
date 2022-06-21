#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    j = 0
    while i < x and x > 0:
        try:
            val = my_list[i]
            if isinstance(val, int):
                print(my_list[i], end='')
                j += 1
            i += 1
        except IndexError:
            break
    print("")
    return int(j)
