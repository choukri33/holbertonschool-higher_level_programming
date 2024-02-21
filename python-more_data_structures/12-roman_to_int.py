#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    numbers = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    pre = 0
    total = 0

    for i in roman_string:
        value = numbers.get(i, 0)
        total += value - 2 * pre if value > pre else value
        pre = value

    return total
