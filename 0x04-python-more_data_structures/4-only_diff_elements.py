#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = []
    for x in (set_1):
        if (list(set_1).count(x) == 1 and list(set_2).count(x) == 0):
            new_list.append(x)
    for k in (set_2):
        if (list(set_2).count(k) == 1 and list(set_1).count(k) == 0):
            new_list.append(k)
    return new_list
