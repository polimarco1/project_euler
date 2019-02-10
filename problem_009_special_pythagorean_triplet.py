"""Botucatu, February 10th 2019
Author: Marco Poli
This program returns the Pytagorean triplet wich sum is a given integer.
"""
from math import sqrt

def pythagorean_triplet(a, b):
    """Returns the sum of a squared and b squared"""
    return sqrt(pow(a, 2) + pow(b, 2))

def pythagorean_sum(num):
    """Check if a + b + c = num"""
    for a in range(3, num-1, 1):
        for b in range(4, num-1, 1):
            c = pythagorean_triplet(a, b)
            if a + b + c == num:
                return a, b, c, a*b*c

    return None


print(pythagorean_sum(1000))
