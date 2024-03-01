#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    romans = {
     "I": 1,
     "V": 5,
     "X": 10,
     "L": 50,
     "C": 100,
     "D": 500,
     "M": 1000
    }

    new_list = [romans[roman_string[0]]]

    for letter in roman_string:
        if romans[letter] > new_list[-1]:
            new_list[-1] *= -1
        new_list.append(romans[letter])
    new_list = new_list[1:]
    sum = 0
    for num in new_list:
        sum += num
    return sum
