#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if (sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
    exit(1)
if sys.argv[1] != ["+", "-", "*", "/"]:
    print("Unknown operator. Available operators: +, -, * and /\n")
    exit(1)
else:
    x = int(sys.argv[0])
    y = int(sys.argv[2])
    op = sys.argv[1]
    if op == "+":
        print("{} + {} = {}".format(x, y, add(x, y)))
    elif op == "-":
        print("{} - {} = {}".format(x, y, sub(x, y)))
    elif op == "/":
        print("{} / {} = {}".format(x, y, div(x, y)))
    elif op == "*":
        print("{} * {} = {}".format(x, y, mul(x, y)))
