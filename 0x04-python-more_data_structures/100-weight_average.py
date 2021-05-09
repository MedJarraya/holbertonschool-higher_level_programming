#!/usr/bin/python3
def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return (0)
    multi = list(map(lambda w: w[0] * w[1], my_list))
    plus = list(map(lambda w: w[1], my_list))
    return sum(multi) / sum(plus)
