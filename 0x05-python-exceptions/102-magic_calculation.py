#!/usr/bin/python3
def magic_calculation(q, d):
    rez = 0
    for i in range(1, 3):
        try:
            if i > q:
                raise Exception("Too far")
            else:
                rez += q ** d / i
        except:
            rez = d + q
            break
    return (rez)
