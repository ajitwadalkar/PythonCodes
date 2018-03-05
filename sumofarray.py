#!/bin/python3

import sys

def simpleArraySum(n, ar):
    # way 1
    # sumOfArr = sum( int(i) for i in ar)

    #way 2
    # sumOfArr = sum(ar)


    #way3
    sumOfArr = 0
    for i in ar:
        sumOfArr += int(i)
    return sumOfArr

n = 6
ar = [12,1,3,57,7,3]
result = simpleArraySum(n, ar)
print(result)
