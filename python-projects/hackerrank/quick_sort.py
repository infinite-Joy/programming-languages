def swap(arr, left, right):
    arr[left], arr[right] = arr[right], arr[left]


def partition(arr, low, high):
    # this is the crux of the algo
    p = high
    firsthigh = low
    for i in range(low, high):
        if arr[i] < arr[p]:
            swap(arr, i, firsthigh)
            firsthigh += 1
    swap(arr, p, firsthigh)
    return firsthigh


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)


arr = [7,6,10,5,9,2,15,7]
print('unsorted arr', arr)
print(quick_sort(arr, 0, len(arr)-1))
print('sorted arr', arr)


# random trials
from random import randint

for _ in range(1000):
    arr = [randint(0, 100000) for _ in range(1000)]
    s_arr = sorted(arr)
    quick_sort(arr, 0, len(arr)-1)
    assert(s_arr == arr)
