#!/usr/bin/python3
"""Define a class 'Square'"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size (int): size of new square
        """
        self.size = size

    def area(self):
        """Return the current area of instance of square"""
        return (pow(self.__size, 2))

    @property
    def size(self):
        """Get te current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """Print square with the charater '#'"""
        if self.__size == 0:
            print()
        else:
            for i in range(pow(self.__size, 2)):
                if (i % self.__size == 0) and i != 0:
                    print()
                print('#', end='')
            print()
