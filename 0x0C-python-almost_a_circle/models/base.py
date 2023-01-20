#!/usr/bin/python3
"""This module creates a class: Base"""


class Base:
    """Creates a base class for other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
