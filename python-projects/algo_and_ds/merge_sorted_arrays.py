from functools import reduce

def merge(arr1, arr2):
    arr1 = list(reversed(arr1))
    arr2 = list(reversed(arr2))
    merged_arr = []
    temp1 = None
    temp2 = None
    while len(arr1) != 0 and len(arr2) != 0:
        if temp1 is None:
            temp1 = arr1.pop()
        if temp2 is None:
            temp2 = arr2.pop()

        if temp1 <= temp2:
            merged_arr.append(temp1)
            temp1 = None
        else:
            merged_arr.append(temp2)
            temp2 = None

    if temp1:
        merged_arr.append(temp1)
    if temp2:
        merged_arr.append(temp2)

    if len(arr1) == 0:
        merged_arr.extend(arr2)
    if len(arr2) == 0:
        merged_arr.extend(arr1)

    return merged_arr


arr1 = [1,3,5,7,9]
arr2 = [2,4,6,8,10]


print(merge(arr1, arr2))


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def sort(a):
    #import time; time.sleep(1)
    #print('a', a)
    if len(a) == 1:
        return a

    half = len(a)//2
    left = sort(a[:half])
    #print('left', left)
    right = sort(a[half:])
    #print('right', right)
    return merge(left, right)

#arr = [1,3,5,7,9] + [2,4,6,8,10]
#print(sort(arr))


def merge(arr, start, mid, end):
    left = start
    right = mid + 1
    pointer = start
    while left <= mid and right < end:
        left_val = arr[left]
        right_val = arr[right]
        if left_val <= right_val:
            arr[pointer] = left_val
            left += 1
            pointer += 1
        else:



def sort(arr, start, end):
    # base case
    if len(arr) <= 1:
        return arr

    mid = start + int((end-start)/2)
    sort(arr, start, mid)
    sort(arr, mid+1, end)
    merge(arr, start, mid, end)
    return arr


arr = "6 31415926535897932384626433832795 1 3 10 3 5"
arr = [int(x) for x in arr.split()]
print(sort(arr))
