#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/test/61sq9qfa63d/questions/472ni48rfm5



# Complete the maxMin function below.
# probably a dp solution exists but that would be O(n2)
# would try to get in  O(n)
# in the first pass find the max and min
# if elem greater than min and element

# 1 2 3 4 10 20 30 40 100 200
#   _                        _
#   110    100     99     200     1000    10   20      30  arr = []
#   [110] max = 110 min = 110
#   [110, 100] max = 110,
#                 [110 100 99] diff = 11

# i think i will have to sort the arr.
# the run through the window with max and min values
# and at the end write  the max and min values

# complexity is O(nlogn)

# if i want to do some subarray maybe i can do something else

def maxMin(k, arr):
    arr.sort()
    minval = arr[0]
    maxval = arr[k-1]
    diff = maxval - minval
    for idx in range(k, len(arr)):
        maxval = arr[idx]
        minval = arr[idx-k+1]
        diff = min(diff, maxval-minval)
    return diff

