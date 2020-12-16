#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_2 = []
    for i in my_list:
        if i % 2:
            div_2.append(False)
        else:
            div_2.append(True)
    return div_2
