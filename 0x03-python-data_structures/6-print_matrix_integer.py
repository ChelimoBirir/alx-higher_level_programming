#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    length = len(matrix)

    for row in range(length):
        for column in range(len(matrix[row])):
            print("{:d}".format(matrix[row][column]), end=" ")
            if column != (len(matrix[row]) - 1):
                print(" ", end='')
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
