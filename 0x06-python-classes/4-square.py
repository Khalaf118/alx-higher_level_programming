#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """ Initialization the new square."""

        self.size = size

    @property
    def size(self):
        """Retrieve the size."""

        return self.__size

    @size.setter
    def size(self, value):
        """Update the size value."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the square area."""

        return self.__size ** 2
