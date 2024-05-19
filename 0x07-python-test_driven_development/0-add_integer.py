#!/usr/bin/python3
"""
a function that adds 2 integers.
args: a, b
return: the sum
"""


def add_integer(a, b=98):
    """
    a function that adds 2 integers and return the sum.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
