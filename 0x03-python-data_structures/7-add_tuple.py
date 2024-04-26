#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    result = tuple(map(sum, zip(tuple_a, tuple_b + (0,) * len(tuple_a))))

    return result
