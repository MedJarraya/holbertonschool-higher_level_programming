#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = []
    for x in set_2:
        for k in set_1:
            if (x == k):
                new_list.append(x)
    return new_list
