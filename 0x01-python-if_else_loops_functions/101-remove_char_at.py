#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    k = len(str)
    for i in range(0, k):
        if i != n:
            newstr = newstr + str[i]
    return(newstr)
