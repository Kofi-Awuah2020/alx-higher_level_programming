#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for columns in row:
            if columns is not row[len(row) - 1]:  # if columns is last element
                print("{:d}".format(columns), end=" ")
            else:
                print("{:d}".format(columns), end="")
        print()
