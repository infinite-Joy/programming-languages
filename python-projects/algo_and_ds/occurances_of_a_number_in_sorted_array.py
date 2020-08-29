"""

Given an array of ages (integers) sorted lowest to highest, output the number of occurrences for each age.
For instance:
[8,8,8,9,9,11,15,16,16,16]
should output something like:
8: 3
9: 2
11: 1
15: 1
16: 3

This should be done in less than O(n).

to do this you can start with index 0
then find the right index of same numver of 0
then we do right - left + 1

then we start from right + 1 and do this again till right < len(arr)

"""

def binary_search(arr, target, low):
    high = len(arr) - 1
    while low < high:
        mid = 1 + (low + high) // 2 # since we are finding the right we can do this
        if arr[mid] > target:
            high = mid - 1
        else:
            low = mid
    return high

def get_counts(arr):
    print(arr)
    if not arr:
        return {}
    if len(arr) == 1:
        return {arr[0]: 1}
    counts = {}
    low = 0
    while low < len(arr):
        target = arr[low]
        high = binary_search(arr, target, low)
        counts[target] = high - low + 1
        low = high + 1
    return counts

arr = [8,8,8, 9, 9, 11, 15, 16, 16, 16]
print(get_counts(arr))
print('#'* 10)

arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42]
print(get_counts(arr))


