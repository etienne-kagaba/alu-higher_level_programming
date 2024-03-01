#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matri = []
    for row in matrix:
        matri.append(row[:])

    for i in range(len(matri)):
        for j in range(len(matri[i])):
            matri[i][j] *= matri[i][j]
    return matri
