#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if (a_dictionary is None):
        return None
    new_dictio = sorted(a_dictionary.keys())
    for x in new_dictio:
        print("{}: {}".format(x, a_dictionary[x]))
