#!/usr/bin/python3
"""
print square
size is the square size
"""


def print_square(size):
    """print square
    size is the square size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for f in range(size):
            print("#", end="")
        print()
