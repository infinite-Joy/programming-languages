#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the minimumPasses function below.
# the guarantee is there that it will run within n // (p*w)
# take the middle value. check if that is possible.
# then do the pivoting accordingly and hence implement a binary search
# m * w = 3 p = 2
# 3 * 1 = 3 => 1
# 3 * 2 = 6 => 7 => 1
# 4 * 5 = 20 > number hence we go to 3
# time complexity is O(n)

# here i am implementing a greedy ssolution

def minimumPasses(m, w, p, n):
    # w to be always less than m
    if m < w:
        m, w = w, m
    running = m * w
    days = 1
    while running < n:
        incr = running // p
        running = running % p
        m += incr // 2
        w += (incr // 2) + (incr % 2)
        running += m * w
        days += 1
        print(running)
    return days

print(minimumPasses(2,1,1,60))
print(minimumPasses(3,1,2,12))
