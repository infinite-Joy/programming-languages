#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
    # 0   0   0   0   0   0   0   0   0   0
    # 3   0   0   0   3   0   0   0   0   0
    # 3   0   0   7   3   0   0   7   0   0
    # 3   0   0   7   3   1   0   7   1   0
# time complexity is O(mlogn)
# space complexity is O(n)
from collections import defaultdict
from bisect import insort
def arrayManipulation(n, queries):
    # print(queries)
    zeros = []
    for idx, (a, b, k) in enumerate(queries):
        insort(zeros, (a, k, 'push'))
        insort(zeros, (b+1, k, 'pop'))
    # print(zeros)
    maxval = 0
    ongoing = 0
    for idx, val, op in zeros:
        if op == 'push':
            ongoing += val
        else:
            ongoing -= val
        # print(ongoing)
        maxval = max(maxval, ongoing)
    return maxval

def arrayManipulation(n, queries):
    # this one can be done in O(n+m)
    # print(queries)
    zeros = [0 for _ in range(n+2)]
    for idx, (a, b, k) in enumerate(queries):
        zeros[a] += k
        zeros[b+1] -= k
    # print(zeros)
    maxval = 0
    ongoing = 0
    for item in zeros:
        ongoing += item
        maxval = max(maxval, ongoing)
        # print(maxval, ongoing)
    return maxval

