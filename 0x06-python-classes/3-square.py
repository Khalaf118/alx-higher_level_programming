#!/usr/bin/python3
# 2-square.py
# Mohamed Khalaf
"""Define a class Square."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """ Initialization the instance.

        Args:
            self: The instance arg.
            size (int): The size of the square.

        Returns:
            No return values; None.

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Returns the square area.

        Args:
            self: The instance arg.

        Returns:
            The square area.

        """

        return self.__size ** 2