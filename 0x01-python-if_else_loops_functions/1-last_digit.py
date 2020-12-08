#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
while n >= 10:
    n = n / 10
if n > 5:
    print("{:d} is greater than 5".format(number))
elif n == 0:
    print("{:d} and is 0".format(number))
else:
    print("{:d} and is less than 6 and not 0".format(number))
