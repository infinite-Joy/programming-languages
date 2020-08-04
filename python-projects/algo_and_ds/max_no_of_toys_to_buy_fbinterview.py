#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the maximumToys function below.

#     1   2   3   4   5   6   7
# 1   1   1   1   1   1   1   1
# 2   1   1   2   2   2   2   2
# 3   1   1   2   2   2   3   3
# 4   1   1   2   2   2   3   3

# recurrence looks like dp[n] = max(dp[n], dp[n-prices[n]])

# 1 12 5 111 200 1000 10

#     1   5   10      12      111     200     1000
# 1
# 5
# 10
# 12
# 111
# 200
# 1000

# time complexity: O(n*k)
# space complexity: O(k)

def maximumToys(prices, k):
    prices.sort()
    dp = [0 for _ in range(k+1)]
    for price in prices:
        for val in range(k, 0, -1):
            if val>=price:
                dp[val] = max(dp[val], dp[val-price]+1)
        print(dp)
    return dp[k]

print(maximumToys([1,2,3,4], 7))
print(maximumToys([1,12,5,111,200,1000,10], 50))

# now using simple iteration
# time complexity: O(n)
# space complexity: O(1)

from itertools import accumulate
from typing import List

def partition(arr: List[int], low: int, high: int):
    p = high
    firsthigh = low
    for i in range(low, high):
        if arr[i] < arr[p]:
            arr[i], arr[firsthigh] = arr[firsthigh], arr[i]
            firsthigh += 1
    arr[p], arr[firsthigh] = arr[firsthigh], arr[p]
    return firsthigh

def qsort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        qsort(arr, low, p-1)
        qsort(arr, p+1, high)

def maximumToys(prices, k):
    qsort(prices, 0, len(prices)-1)
    print(prices)
    prices = accumulate(prices)
    for i, p in enumerate(prices):
        if p > k:
            return i
    return len(prices)


print(maximumToys([1,2,3,4], 7))
print(maximumToys([1,12,5,111,200,1000,10], 50))
