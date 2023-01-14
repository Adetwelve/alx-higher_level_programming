#!/usr/bin/python3
"""Module t create a class: LockedClass"""


class LockedClass:
    """Prevent user from dynamically creating new instance
    attributes, except if the new instance attribute is called
    first_Name"""

    __slots__ = ["first_name"]
