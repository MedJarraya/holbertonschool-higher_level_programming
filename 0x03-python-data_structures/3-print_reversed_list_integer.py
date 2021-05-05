#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        k = len(my_list) - 1
        for i in range(k, -1, -1):
            print("{:d}".format(my_list[i]))
