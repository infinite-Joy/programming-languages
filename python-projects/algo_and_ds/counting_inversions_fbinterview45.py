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

# this is the brute force method
def countInversions(arr):
    # time complexity is O(n2)
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

# using merge sort. doing nlogn
INVERSIONS = 0

def merge(arr1, arr2):
    global INVERSIONS
    i = 0
    j = 0
    output = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            output.append(arr1[i])
            i += 1
        else:
            INVERSIONS += len(arr1) - i
            output.append(arr2[j])
            j += 1
    if i < len(arr1):
        output.extend(arr1[i:])
    if j < len(arr2):
        output.extend(arr2[j:])
    return output

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    low = 0
    high = len(arr)
    mid = (low + high) // 2
    arr1 = merge_sort(arr[low:mid])
    arr2 = merge_sort(arr[mid:high])
    return merge(arr1, arr2)

def countInversions_merge_sort(arr):
    global INVERSIONS
    INVERSIONS = 0
    merge_sort(arr)
    ans = INVERSIONS
    INVERSIONS = 0
    return ans

arr = [2,1,3,1,2]
print(countInversions_merge_sort(arr))

arr = [8, 22, 7, 9, 31, 19, 5, 13]
print(countInversions_merge_sort(arr))
