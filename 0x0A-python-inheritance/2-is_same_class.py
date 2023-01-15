#!/usr/bin/python3
"""Define a class: checking a function"""


def is_same_class(obj, a_class):
    """Check if an object is exactly
    an instance of the specified class

    Args:
        obj (any): The object to check.
        a_class (type): the class to match the type of obj to.
    Returns:
        if obj is exactly an instance of a_class - True
        otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
