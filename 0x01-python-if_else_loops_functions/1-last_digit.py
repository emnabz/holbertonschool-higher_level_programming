#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
if n < 0:
    n = n * -1
while n >= 10:
    n = n % 10
    if number < 0:
        n = n * -1
if n > 5:
    print("Last digit of {:d} is {:d}".format(number, n), end=" ")
    print("and is greater than 5")
if n == 0:
    print("Last digit of {:d} and is 0".format(number))
if n < 6 and n != 0:
    print("Last digit of {:d} is {:d}".format(number, n), end=" ")
    print("and is less than 6 and not 0")
