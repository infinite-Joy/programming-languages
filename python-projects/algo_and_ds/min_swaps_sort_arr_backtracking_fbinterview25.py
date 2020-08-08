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
                #print(first, sec, arr)
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
print(minimumSwaps( [4,3,1,2] ))
print(minimumSwaps( [2,3,4,1,5] ))
print(minimumSwaps( [1,3,5,2,4,6,7] ))
print(minimumSwaps(     [2, 31, 1, 38, 29, 5, 44, 6, 12, 18, 39, 9, 48, 49, 13, 11, 7, 27, 14, 33, 50, 21, 46, 23, 15, 26, 8, 47, 40, 3, 32, 22, 34, 42, 16, 41, 24, 10, 4, 28, 36, 30, 37, 35, 20, 17, 45, 43, 25, 19] ))

###############################

# efficient solution to get this done.
# look at each index and compare the index position with its element value.
# if the index position is not the same as the element value then treat
# element value as the index position to find the next element in the series.
# if we come back to the visited element then there exists a cycle, then count
# the size of the cycle, the number of swaps for thecycle wi=ould be size-1, do
# this for all the cycles and then add them together.

# https://www.youtube.com/watch?v=J9ikRMK8Yhs

def minimum_swaps(arr):
    sorted_arr = [i for i in arr]
    sorted_arr = sorted(sorted_arr)
    sorted_arr = list(enumerate(sorted_arr))
    sorted_arr = {elem: pos for pos, elem in sorted_arr}
    arr = [sorted_arr[e] for e in arr]
    visited = [False for _ in arr]
    count = 0
    for idx, elem in enumerate(arr):
        if idx != arr[idx]:
            while visited[idx] is not True:
                visited[idx] = True
                count += 1
                idx = arr[idx]
    return count - 1




print(minimum_swaps( [7, 1, 3, 2, 4, 5, 6] ))
print(minimum_swaps( [4,3,1,2] ))
print(minimum_swaps( [2,3,4,1,5] ))
print(minimum_swaps( [1,3,5,2,4,6,7] ))
