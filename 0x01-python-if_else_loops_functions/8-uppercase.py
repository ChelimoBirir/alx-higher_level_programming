def uppercase(str):
    ''' changes a string to uppercase
    '''
    for c in str:
        print(chr(ord(c) & ~32).format(), end=', ')
    print()
