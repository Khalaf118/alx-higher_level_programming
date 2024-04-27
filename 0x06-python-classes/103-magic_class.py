#!/usr/bin/python3
"""Magic Class to calculate circle area and circumference"""


import math


class MagicClass:
    """Magic Class to calculate circle area and circumference"""

    def __init__(self, radius=0):
        """Initialization the circle radius.

        Arg:
            radius (float or int): The radius of the new circle.
        """

        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate the circle area"""

        return 2 * math.pi * self.__radius ** 2

    def circumference(self):
        """Calculate the circle circumference"""

        return 2 * math.pi * self.__radius
