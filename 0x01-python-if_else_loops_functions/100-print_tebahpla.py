#!/usr/bin/python3
for i in range(122, 64, -1):
    letter = chr(i)
    if i % 2 == 0:
        letter = letter.upper()
    print("{}".format(letter), end='')
