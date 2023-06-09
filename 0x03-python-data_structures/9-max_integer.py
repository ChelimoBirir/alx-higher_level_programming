#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)

    if length <= 0:
        return (None)

    large = my_list[0]

    for i in my_list:
        if i > large:
            large = i

    return (large)
'''
Write a function that finds the biggest integer of a list.

Prototype: def max_integer(my_list=[]):
If the list is empty, return None
You can assume that the list only contains integers
You are not allowed to import any module
You are not allowed to use the builtin max()
'''
