#!/usr/bin/pyton3
"""Define a function: add_integers"""


def add_integer(a, b=98):
    """adds two integers

    ARgs:
        @a (int, float): oprand 1
        @b (int, float): oprand 2

    Raises:
        TypeError: if either a or b is not an int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')

    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
