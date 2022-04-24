


"""

Quick sort algorithm

pivot is the valuye in the paritioning space for which I want to find the position of.

all the elements to the left of the pivot are less than the pivot

all the elements to the right of the pivot are more than the pivot.

"""

from random import randint


def partition(arr, l, r):
    pivot = r
    i = l
    for j in range(l, r):
        if arr[j] < arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[pivot] = arr[pivot], arr[i]
    return i


def quick_sort(arr, l, r):
    if l < r:
        pivot = partition(arr, l, r)
        quick_sort(arr, l, pivot - 1)
        quick_sort(arr, pivot + 1, r)

def sorting(arr):
    quick_sort(arr, 0, len(arr)-1)
    return arr



import numpy as np
 
arr = np.random.rand(7)
print('unsorted arr', arr)
# p = partition(arr, 0, len(arr))
# print(arr, p)
print('sorting', sorting(arr))
print(sorted(arr))