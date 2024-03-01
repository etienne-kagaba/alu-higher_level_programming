#!/usr/bin/python3
def uppercase(str):
    upper = ""
    letter = ""
    for i in str:
        letter = ord(i)
        if ord(i) in range(97, 123):
            letter -= 32
        upper += chr(letter)
    print("{0:s}".format(upper))
