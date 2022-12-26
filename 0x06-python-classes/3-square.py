#!/usr/bin/python3
"""Define a class 'Square'"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size (int): size of new square
        """

        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of instance of a square"""

        return (pow(self.__size, 2))
