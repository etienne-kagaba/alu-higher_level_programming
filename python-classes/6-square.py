#!/usr/bin/python3
"""This is a module level docstring"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the
        Args:
            size: size of the square
            position: position must be a tuple of 2 positive integers
        """
        self.size = size
        self.position = position

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

    def my_print(self):
        """
        Print the square
        Returns:
            None
        """
        if self.__size > 0:
            print('\n' * self.position[1], end='')
            for i in range(self.__size):
                print(' ' * self.position[0], end='')
                print('#' * self.__size)
        else:
            print('')

    @property
    def position(self):
        """
        Get the position of the square
        Returns:
            The position of the square
        """
        return self.__position

    @position.setter
    def position(self, position):
        """
        Set the position of the square
        Args:
            position: a tuple of 2 positive integers

        Returns:
            None
        """
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (type(position[0]) is int and type(position[1]) is int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
