#!/usr/bin/python3
"""Module to create a function: read_file"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout
    Return none
    """
    with open(filename, encoding="UTF_8") as f:
        print(f.read(), end='')
