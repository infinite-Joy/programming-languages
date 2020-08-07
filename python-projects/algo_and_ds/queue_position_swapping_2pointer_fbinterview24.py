#!/bin/python3

#https://www.hackerrank.com/test/61sq9qfa63d/questions/fbqtijrmgrr

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
# this can be done using the bfs approach
# and that would give us the  minimum number of swaps
# finally trying with a 2 pointer method

# the previous methods are not working.
# saw the solution to this.
def understand(arr):
    count = 0
    for idx, item in enumerate(arr, 1):
        print(idx, item)
        # First check if any P is more than two ahead of
        # its original position
        if (item-idx)>2:
            print("Too chaotic")
            return

        # from here on we dont care if p has moved forwards, probably it is
        # better to see if we can count how many times p has recieved a bribe,
        # doing that we will get to know. p's priginal value is the value of p.
        # anyone who bribed p can only get at max one position infront of p and
        # at least one position before p. so we need to see how many people are
        # there in front of p who are having values larger than p
        # to make sure that we dont try indexes less than 0 we can use the max
        # function.
        for idx2 in range(max(item-2, 0), idx):
            if arr[idx2] > item:
                count += 1

    print(count)
    print()
    print()

def minimumSwaps(q):
    print(q)
    understand(q)

print(minimumSwaps([2,1,5,3,4]))
print(minimumSwaps([2,5,1,3,4]))

# this probably could have been done with a divide and conquer approach.
# will need to look into this.
print(minimumSwaps([1,2,5,3,7,8,6,4]))
