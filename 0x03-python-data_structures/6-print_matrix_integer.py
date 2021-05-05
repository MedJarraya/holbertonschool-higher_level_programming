#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for k in range(len(i)):
            if k != 0:
                print(" ", end='')
            print("{:d}".format(i[k]), end='')
        print()
