#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the repeatedString function below.
def repeatedString(s, n):
    # this is a math problem
    # take the dividend and the remainder
    # in one pass count how many are there in the a in the full string and the substring
    # time complexity O(len(s))

    div = n // len(s)
    rem = n % len(s)

    total_a = 0
    sub_a = 0
    for i, ch in enumerate(s):
        if i == rem:
            sub_a = total_a
        if ch == 'a':
            total_a += 1
    return total_a*div + sub_a

print(repeatedString("aba", 10))
