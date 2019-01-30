"""Davis, January 9th 2019
Author: Marco Poli
This program returns the largest prime factor for a given number.
"""
from math import sqrt

def is_it_prime(num):
    """This function returns True if a integer is prime."""
    if (num != 2 and num % 2 == 0) or num <2:
        return False
    aux = num - 2
    while aux > 2:
        if num % aux == 0:
            return False
        aux -= 2
    return True
        

def largest_prime_factor(num):
    """This fucntion returns the largest prime factor 
    for a given number.
    """
    aux = int(sqrt(num))

    while aux > 0:
        if num % aux == 0 and is_it_prime(aux):
            return aux
        else:
            aux -= 1

    

#print(largest_prime_factor(600851475143))
#print(largest_prime_factor(13195))

for i in range(1,1101,1):
    print("For number {} the largest prime is {}".format(i, \
            largest_prime_factor(i)))
###    print("For number {} the largest prime is {}".format(i, i))
