"""
Thinking is the same as that of the quick sort

"""

def partition(arr, l, r):
    pivot = r
    i = l
    for j in range(l, r):
        if arr[j] < arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[pivot] = arr[pivot], arr[i]
    return i


def find_nth_largest(arr, l, r, target_pos):
    if l < r:
        pivot = partition(arr, l, r)
        if target_pos == pivot:
            return arr[pivot]
        elif target_pos < pivot:
            return find_nth_largest(arr, l, pivot-1, target_pos)
        else:
            return find_nth_largest(arr, pivot+1, r, target_pos)

    # this is the base case
    return arr[l]


def main(arr, n):
    if n >= len(arr):
        return max(arr)
    else:
        target_pos = len(arr) - n
        return find_nth_largest(arr, 0, len(arr)-1, target_pos)


import numpy as np
 
arr = np.random.rand(7)
print('unsorted arr', arr)
# p = partition(arr, 0, len(arr))
# print(arr, p)
print('sorting', main(arr, 2))
print(sorted(arr))