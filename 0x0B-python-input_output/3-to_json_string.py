#!/usr/bin/python3
"""Module to creat afunction: to_json_string"""
import json


def to_json_string(my_obj):
    """A function that  returns JSON rprsntation
    of an objct(string)
    """
    return json.dumps(my_obj)
