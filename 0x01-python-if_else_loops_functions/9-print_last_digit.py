def print_last_digit(a):
    if a < 0:
        nbr = (-a) % 10
    elif a == 0:
        nbr = a
    else:
        nbr = a % 10
    print("{:d}".format(nbr), end='')
    return(nbr)
