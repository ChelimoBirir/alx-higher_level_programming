#!/usr/bin/python3
def uppercase(str):
    ''' changes a string to uppercase
    '''
    for c in str:
        if 97 <= c <= 122:
            print(chr(ord(c) & ~32).format(), end='')
        else:
            print(c, end='')
    print()
