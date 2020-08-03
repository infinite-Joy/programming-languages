#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    # this can be done by keeping track
    # of the alt of the hiker.
    # for all changes from 0 to -, valley_count += 1
    # i can use recursion but that would have the stack as O(n)
    # hence making use of iteration
    # complexity is O(n)
    alt = 0
    val_count = 0
    for trek in s:
        if trek == 'U':
            alt += 1
        if trek == 'D':
            if alt == 0:
                val_count += 1
            alt -= 1
    return val_count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

