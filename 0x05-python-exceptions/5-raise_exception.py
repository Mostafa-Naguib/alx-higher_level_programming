#!/usr/bin/python3
def raise_exception():
    "sf" + 2

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
