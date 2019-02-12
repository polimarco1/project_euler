"""Botucatu, February 11th 2019
Author: Marco Poli
This program gives the highest divisible triangular number.
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

def triangular_number(n):
    return (n*(n+1))/2

def number_of_divisors(num):
    divisors = []
    if num == 1:
        divisors = [1]
        return [num, len(divisors), divisors]
    elif is_it_prime(num):
        divisors = [1, num]
        return [num, len(divisors), divisors]
    else:
        aux = 1
        while aux <= num/2:
            if num % aux == 0:
                divisors.append(aux)
            aux += 1

        divisors.append(num)

        return [num, len(divisors), divisors]

def factorization(num):
    divisors = [1]
    if num == 1:
        return [num, len(divisors), divisors]
    elif is_it_prime(num):
        divisors = [1, num]
        return [num, len(divisors), divisors]
    else:
        aux = num
        count = 2
        while aux != 1:
            if aux % count == 0:
                aux /= count
                divisors.append(count)
            else:
                count += 1

        aux_list =[]

        for i in range(0,len(divisors),1):
            for j in range(i, len(divisors), 1):
                if num % (divisors[i] * divisors[j]) == 0 and (divisors[i] * divisors[j]) not in divisors:
                    divisors.append(divisors[i] * divisors[j])

        divisors.append(num)
        divisors = list(set(divisors))
        divisors.sort()

        return [num, len(divisors), divisors]

n = 1
while True:
    if factorization(triangular_number(n))[1] > 5e2:
        print(number_of_divisors(triangular_number(n)))
        break
    n += 1 
