#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the numberPairs function below.
def numberPairs(n, ar):

    # i can probably use this using a hashset
    # if val not present in hashset add to the hashset
    # else remove from the hash set

    # Write your code here
    unmatched = set()
    matching = 0
    for item in ar:
        if item in unmatched:
            matching += 1
            unmatched.remove(item)
        else:
            unmatched.add(item)
    return matching


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = numberPairs(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
