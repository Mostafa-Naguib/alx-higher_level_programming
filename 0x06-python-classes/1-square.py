#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a square with its attribute."""
    def __init__(self, size):
        """constructor.

        Args:
            size: length of a side of the square.
        """
        self.__size = size
