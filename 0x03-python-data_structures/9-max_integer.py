#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    copy = my_list.copy()
    copy.sort(reverse=True)

    return copy[0]
