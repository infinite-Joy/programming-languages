#!/bin/python3

# https://www.hackerrank.com/test/61sq9qfa63d/questions/472ni48r5qi

import math
import os
import random
import re
import sys



# Complete the getMinimumCost function below.
# if things are 7
# 1 2 3     5 7 9
# first we can sort the list

# so we can do someting like this
# alternate the sides or rotate the arr
# [1 2 3]
# [9 7 5] * 1
#   [1 3] * 2
# so something like how maby times i can cycle through the list

# 5 // 3 + 1
# do a reverse sort
# complexity is O(n)



def getMinimumCost(k, c):
    costs = c
    costs.sort(reverse=True)
    print('costs', costs)
    cycles = len(costs) // k + 1
    print('cycles', cycles)
    min_cost = 0
    for idx, cost in enumerate(costs):
        multiplier = idx // k
        min_cost += (multiplier + 1) * cost

    return min_cost

print(getMinimumCost(3, [2,5,6]))
