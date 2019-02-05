"""Botucatu, February 5th 2019
Author: Marco Poli
This program returns the nths prime.
"""
from math import sqrt

def is_it_prime(num):
    """This function returns True if the integer is prime."""
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

def nth_prime(num):
    """This function returns nths prime."""
    count = 3
    primes = [2]

    while len(primes) < num:
        if is_it_prime(count):
            primes.append(count)
        count += 2

    return primes[len(primes)-1]

print(nth_prime(10001))
