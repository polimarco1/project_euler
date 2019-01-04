"""Davis, January 5th 2019
Author: Marco Poli
This program calculates the sum of the even-valued terms
of the Fibonacci sequence numbers whose values do not exceed
four millon.
"""


def even_fibonacci():
    """This program calculates the sum of the even-valued terms
    of the Fibonacci sequence numbers whose values do not exceed
    four millon.
    """

    num1 = 0
    num2 = 1
    numf = 0
    summation = 0

    while True:
        numf = num1 + num2
        num1 = num2
        num2 = numf

        if numf > 4e6:
            break
        elif numf%2 == 0:
            summation += numf

    return summation


print(even_fibonacci())
