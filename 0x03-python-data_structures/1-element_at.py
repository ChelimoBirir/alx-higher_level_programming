#!/usr/bin/python3
def element_at(my_list, idx):

    length = len(my_list)

    if idx < 0 or idx >= length:
        return None
    else:
        return (my_list[idx])


'''
Write a function that retrieves an element from a list like in C.

Prototype: def element_at(my_list, idx):
If idx is negative, the function should return None
If idx is out of range (> of number of element in my_list),
the function should return None
You are not allowed to import any module
You are not allowed to use try/except
'''
