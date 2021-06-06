#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    k = 0
    for value in range(x):
        try:
            print("{:d}".format(my_list[value]), end="")
            k += 1
        except (TypeError, ValueError):
            pass
    print()
    return (k)
