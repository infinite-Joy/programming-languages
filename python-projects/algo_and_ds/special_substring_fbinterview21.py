#!/bin/python3

import math
import os
import random
import re
import sys



# https://www.hackerrank.com/test/61sq9qfa63d/questions/7tqcfiti3k5
# Complete the substrCount function below.
# right now only the brute force one is coming into mind
# for each target word check if the surrounding words are the same.
# the complexity is O(n)
def builder_count(string: str, left: int, right: int) -> int:
    """build the count where the split is in the middle"""
    count = 0
    while left >= 0 and right < len(string) and (string[left] == string[right]):
            left -= 1
            right += 1
            count += 1
    return count


def substrCount(string: str):
    """Build the substring count"""
    print(string)
    count = 0
    for idx, ch in enumerate(string):
        count += builder_count(string, idx, idx) # odd length
        count += builder_count(string, idx, idx+1) # even length
    return count
print(substrCount("abcbaba"))
print("*"*10)
print(substrCount("aaaa"))

# manacher algorithm

