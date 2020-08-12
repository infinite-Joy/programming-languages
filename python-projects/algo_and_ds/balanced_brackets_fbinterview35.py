#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the isBalanced function below.
def isBalanced(s):
    # the complexity is O(n)
    match = {'}': '{', ']': '[', ')': '('}
    stack = []
    string = s
    for item in string:
        if len(stack) > 0 and item in match and match[item] == stack[-1]:
            stack.pop()
        else:
            stack.append(item)
    return "YES" if not stack else "NO"


