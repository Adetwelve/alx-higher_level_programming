#!/usr/bin/python3
"""This module creates a function: add_attribute"""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if it,s possible

    Args:
        obj (any): The object
        name (str): Name of the attribute
        value (any): Value of attreibute
    Raises:
        TypeError: if the attribute cannot be added
    """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
