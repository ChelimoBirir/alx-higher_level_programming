#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    if num_arguments == 0:
        print("0 arguments.")
    else:
        plural = "s" if num_arguments > 1 else ""

        print("{} argument{}:".format(num_arguments, plural))

        for i, arg in enumerate(arguments):
            print("{}: {}".format(i + 1, arg))
