#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    len1 = len(my_list_1)
    len2 = len(my_list_2)
    if len1 > len2:
        for i in range(len2, len1):
            my_list_2.append(None)
    elif len1 < len2:
        for i in range(len1, len2):
            my_list_1.append(None)
    for i, j in zip(my_list_1, my_list_2):
        # print(f"{i} and {j}")
        try:
            new_list.append(i / j)
        except ZeroDivisionError:
            print('division by 0')
            new_list.append(0)
        except TypeError:
            if None in (i, j):
                print("out of range")
                new_list.append(0)
            else:
                print('wrong type')
        except Exception as e:
            print(e)
    return new_list
