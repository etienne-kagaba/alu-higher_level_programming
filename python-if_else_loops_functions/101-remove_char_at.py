#!/usr/bin/python3
def remove_char_at(str, n):
    num = 0
    copy_str = ""
    for i in str:
        num += 1
    for index in range(num):
        if index == n:
            continue
        copy_str += str[index]
    return copy_str
