#!/usr/bin/python3
# 0-square.py
# Mohamed Khalaf
"""Define a class Square."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """ Initialization the instance.

        Args:
            self: The instance arg, optional=0.
            size: The size of the square.

        Returns:
            No return values; None.

        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
