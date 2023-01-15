#!/usr/bin/python3
"""Defines a class to inherits a class"""


class MyList(list):
    """Creates a new class, MyList that inherits from list"""

    def print_sorted(self):
        """Print the list, but sorted(ascending sort)"""

        print(sorted(self))
