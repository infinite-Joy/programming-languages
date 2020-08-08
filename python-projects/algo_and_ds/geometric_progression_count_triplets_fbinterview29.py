#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the countTriplets function below.
# creating the i and j as the values in the hashmaps
# this is in O(n2) both in time and space
def countTriplets(arr, r):
    print(arr)
    gp = {}
    for idx1 in range(len(arr)):
        for idx2 in range(idx1+1, len(arr)):
            if arr[idx2] / arr[idx1] == r:
                nextval = arr[idx2] * r
                if nextval not in gp:
                    gp[nextval] = 0
                gp[nextval] += 1
    count = 0
    for idx, item in enumerate(arr):
        if item in gp:
            print(gp[item], idx)
            count += gp[item]
    return count

def countTriplets(arr, r):
    # we can also do this using two pointers.
    # time complexity is nlogn for the sorting.
    arr.sort() # this is nlogn
    maxval = arr[-1]
    print(r, arr)
    gp = {}
    i = 0
    j = 1
    count = 0
    # next while loop is in O(n)
    while j < (len(arr)):
        #print(i, j)
        if (arr[j] / arr[i]) == r:
            nextval = r * arr[j]
            if nextval <= maxval:
                if nextval not in gp:
                    gp[nextval] = 0
                gp[nextval] += 1
            j += 1
        elif (arr[j] / arr[i]) < r:
            j += 1
        else:
            i += 1
        #print(gp)

    # checking the value is in O(n)
    print(gp)
    count = 0
    for idx, item in enumerate(arr):
        if item in gp:
            # print(gp[item], idx)
            count += gp[item]
    return count


print(countTriplets([1,2,2,4], 2))
print(countTriplets([1,3,9,9,27,81], 3))
print(countTriplets([1,5,5,25,125], 5))
