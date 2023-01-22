#!/usr/bin/python3
"""Module to create a function: append_write"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file (UTF8)
    returns the number of characters added:
    """
    with open(filename, 'a', encoding="utf-8") as f_a:
        return f_a.write(text)
