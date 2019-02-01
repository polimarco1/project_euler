"""Botucatu, Febuary 1st 2019
Author: Marco Poli
This program finds the difference between the sum
of the squares with the square of the sum for a given number.
"""

def sum_squares(args):
    """This fuction does the sum of squares."""
    summ = 0
    for i in args:
        summ += i**2
    return summ

def squares_sum(args):
    """This fuction does the squares of sum."""
    return sum(args)**2


selection = list(range(1, 101, 1))
sqrsum = squares_sum(selection)
sumsqr = sum_squares(selection)

print("The diference between the squares sum and sum squares is:\n\
{} - {} = {}".format(sqrsum, sumsqr, sqrsum - sumsqr))
