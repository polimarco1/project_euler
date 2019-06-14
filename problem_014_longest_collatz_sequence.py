"""
Davis, June 13th 2019
Author: Marco Poli
This program does the Collatz Sequence
"""
from math import log

def colletz(num):
    mylist = []
    mylist.append(num)
    while num != 1:
        if (log(num,2) - int(log(num,2))) == 0:
            num /= 2
        elif num % 2 == 0:
            num /= 2
        else:
            num = 3*num + 1
        mylist.append(int(num))

    return(mylist)
    
def longest_chain(num):
    mylist1 = []
    mylist2 = []
    for i in range(num,0,-1):
        mylist1 = colletz(i)
        if len(mylist1) > len(mylist2):
            mylist2 = mylist1.copy()
        
    return(mylist2)

anwser = longest_chain(999999)
print("The start number that produces the longest chain with {} elemenst is: {} \
        \nThe full chain is:\n{}".format(len(anwser), anwser[0], anwser))
