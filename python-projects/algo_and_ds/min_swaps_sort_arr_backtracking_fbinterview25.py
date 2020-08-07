#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the minimumSwaps function below.
# we will try using backtracking
# this will go through all the configurations. hence the complexity is O(n2)
def do(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
def undo(arr, i, j):
    do(arr, j, i)
def swaps(arr, count, i, final, minval):
    for first in range(i, len(arr)):
        for sec in range(first, len(arr)):
            if arr[first] > arr[sec]:
                do(arr, first, sec)
                print(first, sec, arr)
                if arr == final:
                    #__import__('pdb').set_trace()
                    minval = min(count+1, minval)
                else:
                    minval = swaps(arr, count+1, first, final, minval)
                undo(arr, first, sec)
    return minval

import math
def minimumSwaps(arr):
    done = [i for i in arr]
    done.sort()
    print(arr)
    return swaps(arr, 0, 0, done, math.inf)

print(minimumSwaps( [7, 1, 3, 2, 4, 5, 6] ))
