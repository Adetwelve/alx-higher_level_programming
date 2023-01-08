#!/usr/bin/python3
"""Define function: say_my_name"""


def say_my_name(first_name, last_name=""):
    """Print fullname of individuals

    Args:
        first_name (str): Indvidual first name
        last_name (str): Individual last name

    Raises:
        TypeError: if any of the name not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
