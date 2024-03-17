#!/usr/bin/python3
"""This is a module level docstring"""


import math


class MagicClass:
    """Magic class"""
    def __init__(self, radius=0):
        """Initialisation of magic class"""
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """Calculates the area of the magic circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates the circumference of the magic cirlce"""
        return (2 * math.pi) * self.__radius
