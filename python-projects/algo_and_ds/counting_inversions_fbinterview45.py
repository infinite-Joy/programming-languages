#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the countInversions function below.
# go forward. if the present is less than the previous one then the
#     do a while loop and then find the lower value and then do a swap.
# 2 1 3 1 2
#     _

def countInversions(arr):
    count = 0
    for idx in range(1, len(arr)):
        prev = idx - 1
        while prev >= 0:
            if arr[idx] < arr[prev]:
                count += 1
            prev -= 1
    return count

arr = [2,1,3,1,2]
print(countInversions(arr))

arr = [8, 22, 7, 9, 31, 19, 5, 13]
print(countInversions(arr))
