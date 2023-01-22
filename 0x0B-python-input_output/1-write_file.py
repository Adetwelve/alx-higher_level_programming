#!/usr/bin/python3
"""Module to create a function: write_file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
    returns the numberof characters written:"""

    with open(filename, 'w', encoding="utf-8") as f_w:
        return f_w.write(text)
