"""Davis, February 10th 2019
Author: Marco Poli
This program returns the summation of all
primes bellow a given integer number.
"""
from math import sqrt

def is_it_prime(num):
    """This function returns True if a integer is prime."""
    if (num != 2 and num % 2 == 0) or num < 2:
        return False

    aux = int(sqrt(num))

    if aux % 2 == 0:
        aux -= 1

    while aux > 2:
        if num % aux == 0:
            return False
        aux -= 2

    return True

def summation_of_primes(num):
    """This function returns the summation of primes
    for a given integer.
    """
    aux = 3
    summ = 2

    while aux <= num:
        if is_it_prime(aux):
            summ += aux
        aux += 2

    return summ

print(summation_of_primes(2e6))
