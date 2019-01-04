"""Davis, January 4th 2019
Author: Marco Poli
This program returns the sum of all multiples of 3 or 5
below a given number.
"""


def multiples_3_or_5(num):
    """This function returns the sum of all multiples of 3 or 5
    below a given number.
    """
    summation = 0
    for i in range(num):
        if i%3 == 0 or i%5 == 0:
            summation += i
    return summation


print(multiples_3_or_5(1000))
