#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if (len(i) == 0 and len(matrix) == 1):
            print('')
            break
        for j in range(len(i)):
            if j == len(i) - 1:
                print("{:d}".format(i[j]))
                break
            print("{:d}".format(i[j]), end=' ')
