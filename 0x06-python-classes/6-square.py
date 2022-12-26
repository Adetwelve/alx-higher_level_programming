#!/usr/bin/python3
"""Define a class 'Square'"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square.

        Args:
            size (int): size of new square
            position (tuple): cordinates to lacate square
        """
        self.size = size
        self.position = position

    def area(self):
        """Return the current area of instance of square"""
        return (pow(self.__size, 2))

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """Get te current size of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        i, j = value
        if isinstance(i, int) and isinstance(j, int):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        if i < 0 or j < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Print square with the charater '#'"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for i in range(pow(self.__size, 2)):
                if (i % self.__size == 0):
                    if i != 0:
                        print()
                    for i in range(self.__position[0]):
                        print(' ', end='')
                print('#', end='')
            print()
