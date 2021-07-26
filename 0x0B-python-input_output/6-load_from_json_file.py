#!/usr/bin/python3
"""
object out of JSON file
"""


import json


def load_from_json_file(filename):
    """object out of JSON file"""
    with open(filename, 'r') as f:
        load_json = json.load(f)
        return(load_json)
