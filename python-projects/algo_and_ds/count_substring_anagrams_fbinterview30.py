#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagramPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
from itertools import combinations

def anagramPairs(s):
    # Write your code here
    # complexity is n!
    string = s
    print(string)
    #string = sorted(string)
    count = 0
    subs = {}
    for r in range(len(string)):
        for substring in combinations(string, r):
            substring = "".join(substring)
            if substring not in subs:
                subs[substring] = 0
            else:
                subs[substring] += 1
            print(substring, subs)
    print(subs)
    return sum(subs.values())


print(anagramPairs("abba"))
#print(anagramPairs("abcd"))
#print(anagramPairs("ifailuhkqq"))
#print(anagramPairs("kkkk"))
#print(anagramPairs("cdcd"))
