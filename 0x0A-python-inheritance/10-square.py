#!/usr/bin/python3
"""Defines a class: Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines the subclass: Square """

    def __init__(self, size):
        """Initialize a square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """computes the are of the square"""

        return pow(self.__size, 2)
