#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        ln = my_list[0]
        for element in my_list:
            if ln < element:
                ln = element
    else:
        return(None)
    return(ln)
