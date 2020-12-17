#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    div = sum(i[1] for i in my_list)
    mul = [(i[0] * i[1]) for i in my_list]
    total = sum(mul)
    result = total / div
    return result
