#!/usr/bin/python3
"""module to create a function: from_json_string"""
import json


def from_json_string(my_str):
    """a function that returns an object
    represented by a JSON string:
    """
    return json.loads(my_str)
