#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_value = 0
    max_key = None
    for k, v in a_dictionary.items():
        if v > max_value:
            max_value = v
            max_key = k
    return k
