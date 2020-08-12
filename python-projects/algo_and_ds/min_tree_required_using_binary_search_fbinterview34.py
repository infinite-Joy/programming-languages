#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minTime function below.
# so what can be done is that a kind of binary search can be done on the machines
# we double the number of days till we get the lower and the upper half and then do a binary search
# to find the actual number of days
# time complexity is or rather mlog(g)
def check_days(machines, days):
    workdone = [days // x for x in machines]
    workdone = sum(workdone)
    return workdone

def binary_search(machines, goal, low, high): # 5
    print(machines, goal, low, high)
    # between 5 and 10
    # between 7 aand 10
    if low + 1 == high:
        return high
    mid = (low+high)//2
    if check_days(machines, mid) < goal:
        # 5 out 3 < goal
        # 7 out 5 <= goal
        return binary_search(machines, goal, mid, high)
    else:
        return binary_search(machines, goal, low, mid)

def minTime(machines, goal):
    low = 0
    high = goal * machines[0]

    print(check_days(machines, low))
    print(check_days(machines, high))
    assert check_days(machines, low) <= goal
    assert check_days(machines, high) >= goal

    return binary_search(machines, goal, low, high)


machines = [2,3]
print(minTime(machines, 5))
machines = [1,3,4]
print(minTime(machines, 10))

machines = [4,5,6]
print(minTime(machines, 12))
