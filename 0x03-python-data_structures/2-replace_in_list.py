#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    new_list = my_list
    if idx < 0:
        return my_list
    elif idx not in range(len(my_list)):
        return my_list
    else:
        new_list[idx] = element
        return new_list
