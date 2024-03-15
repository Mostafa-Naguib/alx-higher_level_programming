#!/usr/bin/python3
import sys

def main():
    list = sys.argv
    num = len(list) - 1
    if num == 0:
        print("0 arguments.")
    elif num == 1:
        print("1 argument: ")
        print("{:d}: {}".format(1, list[1]))
    else:
        print("{:d} arguments:".format(num))

        for i in range(1, num+1):
            print("{:d}: {}".format(i, list[i]))

if __name__ == "__main__":
    main()
