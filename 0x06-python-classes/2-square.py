#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a square with its attribute"""
    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of a side of the square.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
