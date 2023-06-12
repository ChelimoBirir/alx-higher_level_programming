#!/usr/bin/python3
def no_c(my_string):

    new_string = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(new_string))


'''
Write a function that removes all characters c and C from a string.

Prototype: def no_c(my_string):
The function should return the new string
You are not allowed to import any module
You are not allowed to use str.replace()
'''
