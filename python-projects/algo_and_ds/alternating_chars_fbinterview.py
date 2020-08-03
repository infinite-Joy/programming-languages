#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    # this can be done with the two pointer method
    # if j value not same as i value then incr counter
    i = 0
    delt = 0
    for j in range(len(s)):
        if j > i:
            if s[i] == s[j]:
                delt += 1
            else:
                i = j
    return delt

