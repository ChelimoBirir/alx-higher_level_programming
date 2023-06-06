#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number >= -9) and (number <= 9):
    print("Last digit of {} is {} and is {}"
          .format(number, number, number), end=' ')
else:
    last_digit = number - (10 * int(number / 10))
    print("Last digit of {} is {}".format(number, last_digit), end=' ')

    if last_digit == 0:
        print("and is 0")
    elif last_digit > 5:
        print("and is greater than 5")
    else:
        print("and is less than 6 and not 0")
