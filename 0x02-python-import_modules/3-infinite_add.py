#!/usr/bin/bash

if __name__ == "__main__":
    import sys

    arguments = sys.argv[1:]

    result = 0
    for i in range(len(arguments)):
        result += int(arguments)
    print("{}".format(result))
