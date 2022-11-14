#!/usr/bin/python3

'''
-Write a class `MyList` that inherits from `list`:
    -Public instance method: `def print_sorted(self):` that
    prints the list, but sorted (ascending sort)
    -You can assume that all the elements of the list will be of type `int`
'''


class MyList(list):
    '''docstring for MyList'''
    def print_sorted(self):
        '''prints the list, but sorted (ascending sort)'''
        list_tmp = self[:]
        list_tmp.sort()
        print(list_tmp)
