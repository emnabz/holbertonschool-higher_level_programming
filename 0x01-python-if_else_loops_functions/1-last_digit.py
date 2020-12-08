#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
i = 1
while n >= 10:
    n = n / 10
    i = i * 10
n = number % i
if n > 5:
    print(" the last digit of {:d} is {:d} is greater than 5".format(number, n))
elif n == 0:
    print("the last digit of {:d} is {:d} and is 0".format(number, n))
elif n < 6 and n != 0:
    print("the last digit of {:d} is {:d} and is less than 6 and not 0".format(number, n))
