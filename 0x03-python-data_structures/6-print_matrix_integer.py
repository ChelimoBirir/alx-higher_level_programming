#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for num in row:
            print("{:d}".format(num), end=" ")
        print()


'''
Write a function that prints a matrix of integers.

Prototype: def print_matrix_integer(matrix=[[]]):
Format: see example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integersi
'''
