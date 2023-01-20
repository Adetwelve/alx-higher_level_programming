#!/usr/bin/python3
"""This module create a class: Rectangl"""


class Rectangle(Base):
    """Defines a nw rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = heigth
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError('width must be an intger')
        elif width <= 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @hight.setter
    def width(self, width):
        if type(hight) != int:
            raise TypeError('height must be an intger')
        elif height <= 0:
            raise ValueError('height must be >= 0')
        self.__height = height

     @property
     def x(self):
         return self.__x

     @x.setter
     def x(self, x):
         if type(x) != int:
            raise TypeError('x must be an intger')
        elif x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y
