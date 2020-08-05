#!/bin/python3
#https://www.hackerrank.com/test/61sq9qfa63d/questions/a1pql08s9i1

import math
import os
import random
import re
import sys



# Complete the twoStrings function below.
def twoStrings(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    chars = {}
    for ch in s1:
        chars[ch] = True

    for ch in s2:
        if ch in chars:
            return "YES"
    return "NO"

