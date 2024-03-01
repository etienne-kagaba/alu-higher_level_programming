#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    newt = ()
    if len1 > 1 and len2 > 1:
        newt = (tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]),
    elif len1 > 1 and len2 == 1:
        newt = (tuple_a[0] + tuple_b[0]), (tuple_a[1]),
    elif len1 > 1 and len2 == 0:
        newt = (tuple_a[0]), (tuple_a[1]),
    elif len1 == 1 and len2 > 1:
        newt = (tuple_a[0] + tuple_b[0]), (tuple_b[1]),
    elif len1 == 0 and len2 > 1:
        newt = (tuple_b[0]), (tuple_b[1]),
    elif len1 == 0 and len2 == 0:
        newt = 0, 0,
    elif len1 == 1 and len2 == 1:
        newt = (tuple_a[0] + tuple_b[0]), 0,
    else:
        pass
    return newt
