#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    new_matrix = []
    temp = []
    for submatrix in matrix:
        for element in submatrix:
            temp.append(element ** 2)
        new_matrix.append(temp)
        temp = []

    return new_matrix
