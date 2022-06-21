#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while i < x and x > 0:
        try:
            print(my_list[i], end='')
            i += 1
        except Exception as e:
            break
    print("")
    return int(i)
