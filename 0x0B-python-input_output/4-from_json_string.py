#!/usr/bin/python3
""" This module defines the function from_json_string. """
import json


def from_json_string(my_str):
    """From JSON to Object"""
    json_obj = json.loads(my_str)
    return(json_obj)
