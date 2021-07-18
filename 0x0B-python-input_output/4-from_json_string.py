#!/usr/bin/python3
"""
From JSON to Object
"""


import json


def from_json_string(my_str):
    """From JSON to Object"""
    json_obj = json.loads(my_str)
    return(json_obj)
