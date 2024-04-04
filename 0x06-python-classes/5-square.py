#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a square with its attribute, method, getter and setter"""
    def __init__(self, size):
        """Constructor.

            Args:
                size: length of a side of the square.

        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")

        if new_size < 0:
            raise ValueError("size must be >= 0")

        self.__size = new_size
    
    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(self.size):
            print("#" * i)

        print()
