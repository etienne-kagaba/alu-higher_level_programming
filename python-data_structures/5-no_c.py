#!/usr/bin/python3
def no_c(my_string):
    newstr = []
    for i in my_string:
        if i in "cC":
            continue
        newstr.append(i)
    newstr = "".join(newstr)
    return newstr
