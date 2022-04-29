"""
sort the arr

for i in the arr


"""

import math


def three_sum_closest(arr, target):
    if len(arr) == 3:
        return sum(arr)

    arr.sort()
    closest = math.inf # i, j, k, sum
    total = 0
    for i in range(len(arr)-2):
        lo = i + 1
        hi = len(arr) - 1
        while lo < hi:
            curr = arr[i] + arr[lo] + arr[hi]
            print(i, lo, hi, curr)
            if curr < target:
                lo += 1
            elif curr > target:
                hi -= 1
            else:
                return target
            if min(closest, abs(target - curr)) < closest:
                closest = min(closest, abs(target - curr))
                total = curr
    return total

arr = [-1,2,1,-4]
target = 1
print(three_sum_closest(arr, target))