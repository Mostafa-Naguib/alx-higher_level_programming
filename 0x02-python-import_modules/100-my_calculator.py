#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        x = int(sys.argv[1])
        y = int(sys.argv[3])
        op = sys.argv[2]
        if op == "+":
            print("{} + {} = {}".format(x, y, add(x, y)))
        elif op == "-":
            print("{} - {} = {}".format(x, y, sub(x, y)))
        elif op == "/":
            print("{} / {} = {}".format(x, y, div(x, y)))
        elif op == "*":
            print("{} * {} = {}".format(x, y, mul(x, y)))
