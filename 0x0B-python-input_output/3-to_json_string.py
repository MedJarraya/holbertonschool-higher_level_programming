#!/usr/bin/python3
"""
JSON of an objet
"""

import json


def to_json_string(my_obj):
    """returns the JSON of an objet"""
    json_string = json.dumps(my_obj)
    return(json_string)
