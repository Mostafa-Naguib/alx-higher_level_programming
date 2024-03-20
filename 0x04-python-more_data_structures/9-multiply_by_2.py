#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    x_dictionary = a_dictionary.copy()
    for key in a_dictionary.keys():
        x_dictionary.update({key: a_dictionary[key] * 2})
    return x_dictionary
