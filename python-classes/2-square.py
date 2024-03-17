#!/usr/bin/python3
"""This is a module level docstring"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0):
        """
        Initialize the
        Args:
            size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
