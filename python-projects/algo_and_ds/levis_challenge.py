


"""

Quick sort algorithm

pivot is the valuye in the paritioning space for which I want to find the position of.

all the elements to the left of the pivot are less than the pivot

all the elements to the right of the pivot are more than the pivot.

"""

from random import randint


def partition(arr, l, r):
    if l == r:
        return 1
    if l < r:
        pivot = r
        firsthigh = l
        for j in range(l, r):
            if arr[j] < arr[pivot]:
                arr[firsthigh], arr[j] = arr[j], arr[firsthigh]
                firsthigh += 1
        # arr[i], arr[pivot] = arr[pivot], arr[i]
        return partition(arr, l, firsthigh-1) + 1
    return 0


def find_arr(arr):
    return partition(arr, 0, len(arr)-1)


arr = [2,3,1,9,7,6]
print(find_arr(arr))

arr = [1,3,2,9,7,6]
print(find_arr(arr))