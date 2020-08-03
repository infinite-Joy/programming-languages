#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # we can implement kind of a greedy solution there
    # there we will jump 2 unless the next 2 is 1
    # so can iterate on the cloud and make the next jump
    pos = 0
    jumps = 0
    while pos < len(c):
        if pos + 2 < len(c) and c[pos+2] == 0: # only if the position is present and the position is safe
            pos += 2
        else:
            pos += 1
        jumps += 1
        print(pos, jumps)
    print(jumps-1)
    return jumps-1


jumpingOnClouds([0,0,0,1,0,0])
