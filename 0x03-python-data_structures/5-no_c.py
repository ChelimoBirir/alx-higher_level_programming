#!/usr/bin/python3
def no_c(my_string):

    new_string = ''

    for char in my_string:
        if (char != 'c') or (char != 'C'):
            new_string += char

    return (new_string)


'''
Write a function that removes all characters c and C from a string.

Prototype: def no_c(my_string):
The function should return the new string
You are not allowed to import any module
You are not allowed to use str.replace()
'''
