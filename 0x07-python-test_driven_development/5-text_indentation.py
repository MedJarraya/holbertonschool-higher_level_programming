#!/usr/bin/python3
"""
text indention function
text is the string to be treated
"""


def text_indentation(text):
    """ text indention function
    text is the string to be treated """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    cond = ['.', ',', '?', ':']
    char = 0
    while char < len(text):
        print("{}".format(text[char]), end="")
        if text[char] in cond:
            print()
            print()
            char += 1
        char += 1
    print()
