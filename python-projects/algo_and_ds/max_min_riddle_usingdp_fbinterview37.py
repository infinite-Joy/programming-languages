#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the riddle function below.
# this can be done using stacks
# complexity is O(n . m)
# this is probably a dp solution

#     2   6   1   12
# 1   2   6   1   12      max = 12
# 2       2   1   1       max = 2
# 3           1   1       max = 1
# 4               1       max = 1

def riddle(arr):
    # complete this function
    n = len(arr)
    windows_stack = [arr[i] for i in range(n)]
    print(windows_stack)
    maxmins = [max(arr)]
    for window in range(n-1):
        maxmin = 0
        for idx in range(n-1, window, -1):
            windows_stack[idx] = min(windows_stack[idx], windows_stack[idx-1])
            maxmin = max(maxmin, windows_stack[idx])
        maxmins.append(maxmin)
        print(windows_stack)
    return maxmins


arr = [2,6,1,12]
print(riddle(arr))

arr = [6,3,5,1,12]
print(riddle(arr))

arr = [1,2,3,5,1,13,3]
print(riddle(arr))

arr = [3,5,4,7,6,2]
print(riddle(arr))
