#!/usr/bin/python3
def safe_print_division(a, b):
    product = None
    try:
        product = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(product))
    return product
