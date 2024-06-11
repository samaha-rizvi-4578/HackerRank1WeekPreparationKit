#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    neg = 0
    pos = 0
    zero = 0
    for i in range(n):
        if arr[i] < 0:
            neg +=1
        elif arr[i] > 0:
            pos +=1
        else:
            zero +=1
    print("{0:.6f}".format(pos/n))
    print("{0:.6f}".format(neg/n))
    print("{0:.6f}".format(zero/n))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
