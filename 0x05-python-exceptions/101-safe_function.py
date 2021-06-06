#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        x = fct(*args)
        return (x)
    except Exception as error:
        sys.stderr.write("Exception: {}\n".format(error.args[0]))
        return (None)
