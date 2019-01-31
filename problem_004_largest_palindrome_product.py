"""Botucatu, January 30th 2019
Author: Marco Poli
This program returns the largest palindrome
made from the product of a given digit
"""

def largest_palindrome_product(digit):
    """This fuction returns the largest palindrome
    made from the product of a given digit
    """
    num1 = pow(10, digit) -1
    num2 = num1
    mylist = []
    for i in range(num1, 0, -1):
        for j in range(num2, 0, -1):
            if str(i*j)[::] == str(i*j)[::-1]:
                mylist.append(i*j)
        num1 -= 1
        num2 -= 1

    return max(mylist)

print(largest_palindrome_product(3))
