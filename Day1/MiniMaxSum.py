#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

# Insertion sort in Python


def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key
    return array

def miniMaxSum(arr):
    # Write your code here
    # first sort the arr
    array = insertionSort(arr)
   #minimum sum (sum of the first four elements)
    min_sum = sum(arr[:4])
    
    # Calculate the maximum sum (sum of the last four elements)
    max_sum = sum(arr[1:])
    
    # Print the results
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
