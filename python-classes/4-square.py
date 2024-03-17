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
        self.__size = size

    def area(self):
        """
        Calculate the Area of the square
        Returns:
            The Area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Get the size of the square
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Set the size of the square
        Args:
            size: size of the square

        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
