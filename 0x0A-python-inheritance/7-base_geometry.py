#!/usr/bin/python3
"""Defines an empty class"""


class BaseGeometry:
    """ Defines the class: BaseGeometry """

    def area(self):
        """returns the area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """"validate value"""

        if type(value) != int:
            raise TypeError(name + ' must be an integer')

        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
