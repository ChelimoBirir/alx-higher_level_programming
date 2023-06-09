#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_string)

    if (idx < 0) or (idx >= length):
        return (my_list)

    for item in my_list:
        if item == my_list[idx]:
            del(item)

    return (my_list)


'''
Write a function that deletes the item at a specific position in a list.

Prototype: def delete_at(my_list=[], idx=0):
If idx is negative or out of range, nothing change (returns the same list)
You are not allowed to use pop()
You are not allowed to import any module
'''
