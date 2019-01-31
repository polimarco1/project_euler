"""Botucatu, January 31st 2019
Author: Marco Poli
This program returns the smallest positive number that can be
dividide from 1 to a given integer number.
"""

def smallest_multiple(num):
    """This program returns the smallest positive number that can be
    dividide from 1 to a given integer number.
    """
    if num <= 0 or isinstance(num, float):
        return "This is not a valid number."

    dividend = num
    divider = 1
    count = 0

    while True:
        if dividend % divider == 0:
            count += 1
            divider += 1
            if count == num:
                return dividend
        else:
            count = 0
            divider = 1
            dividend += 1

print(smallest_multiple(20))
