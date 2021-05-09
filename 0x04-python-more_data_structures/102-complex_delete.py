#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if (a_dictionary is None or len(a_dictionary) == 0):
        return a_dictionary
    del_items = []
    for k, z in a_dictionary.items():
        if (z == value):
            del_items.append(k)
    for x in del_items:
        del a_dictionary[x]
    return a_dictionary
