#!/usr/bin/python3
def safe_print_division(q, d):
    try:
        k = q / d
    except ZeroDivisionError:
        k = None
    finally:
        print("Inside result: {}".format(k))
    return (k)
