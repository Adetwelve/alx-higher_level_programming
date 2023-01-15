#!/usr/bin/python3
"""Defines an object attribute lookup function"""

def lookup(obj):
    """Returns a list of an object's available attributes and method"""

    return dir(obj)
