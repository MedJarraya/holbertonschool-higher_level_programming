#!/usr/bin/python3
def roman_to_int(roman_string):
    if(type(roman_string) != str or roman_string is None):
        return (0)
    my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    z = ""
    w = 0
    rez = 0
    for k in range(len(roman_string)):
        z = roman_string[k]
        if (len(roman_string) != k + 1 and my_dict[roman_string[k + 1]] >
           my_dict[z]):
            w = my_dict[z]
        rez += my_dict[z]
        rez -= w
    return (rez)
