#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """ Initialization the new square."""

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position"""

        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and len(value) == 2
                and isinstance(value[0], int) and isinstance(value[1], int)
                and value[0] >= 0 and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Returns the square area."""

        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #."""

        if self.__size == 0:
            print()
        else:
            for r in range(self.__position[1]):
                print()

            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
