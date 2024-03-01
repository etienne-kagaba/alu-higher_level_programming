#!/usr/bin/python3
def max_integer(my_list=[]):
    maxval = 0
    if len(my_list) == 0:
        return None
    else:
        maxval = my_list[0]
        for i in my_list:
            if i > maxval:
                maxval = i
        return maxval
