"""Davis, January 4th 2019
Author: Marco Poli
This program returns the sum of all multiples of 3 or 5 below 1000
"""


def multiples_3_and_5(num):
    """This function returns the sum of all multiples of 3 or 5
    below a given number
    """
    soma = 0
    for i in range(num):
        if i%3 == 0 or i%5 == 0:
            soma += i
    return soma


print(multiples_3_and_5(1000))
