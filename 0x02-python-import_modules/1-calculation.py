#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
def main():
    sum = add(10, 5)
    difference = sub(10, 5)
    product = mul(10, 5)
    quotient = div(10, 5)


    print("10 + 5 = {:d}".format(sum))
    print("10 - 5 = {:d}".format(difference))
    print("10 * 5 = {:d}".format(product))
    print("10 / 5 = {:d}".format(quotient))

if __name__ == "__main__":
    main()
