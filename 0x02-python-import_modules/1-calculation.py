#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    """This is a test for calculator_1 module"""
    a = 10
    b = 5
    sum = add(a, b)
    difference = sub(a, b)
    product = mul(a, b)
    quotient = div(a, b)


    print("{} + {} = {:d}".format(a, b, sum))
    print("{} - {} = {:d}".format(a, b, difference))
    print("{} * {} = {:d}".format(a, b, product))
    print("{} / {} = {:d}".format(a, b, quotient))
