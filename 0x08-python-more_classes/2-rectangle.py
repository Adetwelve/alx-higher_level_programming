#!/usr/bin/python3
"""Module to create an empty class
"""


class Rectangle():
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle
        Args:
            width: Breath of rectangle
            height: length of rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
        """Return area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Return perimeter of the rectangle"""
        if not self.__width or not self.__height:
            return 0

        return 2 * (self.__height + self.__width)
