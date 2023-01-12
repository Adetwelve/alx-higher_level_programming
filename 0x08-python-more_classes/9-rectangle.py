#!/usr/bin/python3
"""Module to create an empty class
"""


class Rectangle():
    """Defines a rectangle
    Attributes:
        number_of_instances (int): The number of Rectangle instance.
        print_symbol (any): The symbol used for the string representation.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a rectangle
        Args:
            width: Breath of rectangle
            height: length of rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Print the Rectangle using # character"""
        for i in range(self.area()):
            if i and not (i % self.width):
                print()
            print(self.print_symbol, end='')
        return ''

    def __repr__(self):
        """Return string representation of the Rectangle."""
        a = str(self.__width)
        b = str(self.__height)

        return 'Rectangle(' + a + ','' ' + b + ')'

    def __del__(self):
        """Print a message for every deletion of Rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return biggest rectangle based on arae"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')

        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an istance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """return a new Rectangle instance"""
        return cls(size, size)
