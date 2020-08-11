#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the activityNotifications function below.
# we can create a binary tree with the median in the root.
# as and when we move the rolling function we remove the value and add the new value.
# we can try rebalancing but this is too much effort. lets think of something else

# this can be done using the running median problem.
# in this case the max heap will be .
# we will also need to remove the element from the heap.
# so we can be using the binary search to find the element in the arr.

# you can do both using bisect. that is like n log k

#https://www.hackerrank.com/test/61sq9qfa63d/questions/ghdqs48nmtb

import bisect

def check_median(arr, curr_el):
    mid = len(arr)
    if len(arr) % 2 == 1:
        med_idx = len(arr) // 2
        return arr[med_idx] * 2 <= curr_el
    else:
        med_idx1 = len(arr) // 2
        med_idx2 = 1 + len(arr) // 2
        return (arr[med_idx1] + arr[med_idx2]) <= curr_el

def remove_oldest(expenditure, sorted_arr, idx, d):
    outgoing = expenditure[idx - d]
    outgoing_idx = bisect.bisect_left(sorted_arr, outgoing)
    sorted_arr.pop(outgoing_idx)

def activityNotifications(expenditure, d):
    sorted_arr = []
    count = 0
    for idx, exp in enumerate(expenditure):
        print(idx, expenditure, sorted_arr)
        if len(sorted_arr) < d:
            bisect.insort(sorted_arr, exp)
        else:
            if check_median(sorted_arr, exp) is True:
                count += 1
            remove_oldest(expenditure, sorted_arr, idx, d)
            bisect.insort(sorted_arr, exp)
    return count

print(activityNotifications([2,3,4,2,3,6,8,4,5], 5))

# we can also be using the 2 heap method.

from heapq import heappop, heappush
import math

def find_median(maxheap, minheap):
    if maxheap and minheap:
        if len(maxheap) == len(minheap):
            return (-1*maxheap[0] + minheap[0]) / 2
        elif len(maxheap) > len(minheap):
            return -1 * maxheap[0]
        else:
            return minheap[0]
    return math.inf

def build_heaps(maxheap, minheap, total_size, incoming_elem, outgoing_elem=None):
    """
    maxheap is for the smaller elements
    minheap is for the larger half of the elements.

    print(activityNotifications([2,3,4,2,3,6,8,4,5], 5))
    """
    diff = total_size % 2 # the difference between the 2 heaps would be either 0 or 1
    currmedian = find_median(maxheap, minheap)

    # add the incoming element
    if incoming_elem > currmedian:
        heappush(minheap, incoming_elem)
    else:
        heappush(maxheap, -incoming_elem)

    # remove the outgoing element
    if outgoing_elem is not None:
        if -outgoing_elem in maxheap:
            maxheap.remove(-outgoing_elem)
        else:
            minheap.remove(outgoing_elem)

    # resize the two heaps
    if len(maxheap) - len(minheap) > diff:
        elem = -1*heappop(maxheap)
        heappush(minheap, elem)
    elif len(minheap) - len(maxheap) > diff:
        elem = heappop(minheap)
        heappush(maxheap, -elem)
    else:
        pass

    return find_median(maxheap, minheap), maxheap, minheap

def check_median(maxheap, minheap, curr_el):
    median = find_median(maxheap, minheap)
    return median * 2 <= curr_el

def activityNotifications(expenditure, d):
    maxheap = []
    minheap = []
    count = 0
    for idx, exp in enumerate(expenditure):
        print(idx, expenditure, maxheap, minheap)
        if idx < d:
            median, maxheap, minheap = build_heaps(maxheap, minheap, d, exp, None)
        else:
            # first check the curr median
            if check_median(maxheap, minheap, exp) is True:
                count += 1

            # then check the next median
            median, maxheap, minheap = build_heaps(
                maxheap, minheap, d, exp, expenditure[idx-d])
        print(median)

    print(idx, expenditure, maxheap, minheap)
    return count


print(activityNotifications([2,3,4,2,3,6,8,4,5], 5))
