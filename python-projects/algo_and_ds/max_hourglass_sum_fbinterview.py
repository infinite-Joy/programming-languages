#!/bin/python3

import math
import os
import random
import re
import sys

# complexity : O(n*m)
# space complexity: O(1)



# Complete the hourglassSum function below.
def hgsum(arr):
    for row in range(len(arr) - 2):
        for col in range(len(arr[0]) - 2):
            yield sum(arr[row][col:col+3]) + arr[row+1][col+1] + sum(arr[row+2][col:col+3])

def hourglassSum(arr):
    maxsum = -float('inf')
    for val in hgsum(arr):
        if maxsum < val:
            maxsum = val
    return maxsum

if __name__ == '__main__':
