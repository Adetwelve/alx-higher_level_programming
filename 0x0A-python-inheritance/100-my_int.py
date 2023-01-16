#!/usr/bin/python3
"""creates a class: 'MyInt'"""


class MyInt(int):
    """Returns the inverse of '==' and '!=' oprators"""

    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return super().__eq__(other)
