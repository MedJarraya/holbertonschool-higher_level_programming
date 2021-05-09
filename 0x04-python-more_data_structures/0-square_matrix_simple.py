#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in range(len(matrix)):
        row = []
        for k in range(len(matrix[x])):
            row.append(matrix[x][k] ** 2)
        new_matrix.append(row)
    return(new_matrix)
