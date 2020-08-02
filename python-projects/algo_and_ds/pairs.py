def merge(arr1, arr2):
    """
    merge two sorted arrays

    Args:
        arr1 (list): first sorted array
        arr2 (list): the second sorted array

    Returns:
        list, the full sorted arr

    """
    i = 0
    j = 0
    sol = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            sol.append(arr1[i])
            i += 1
        else:
            sol.append(arr2[j])
            j += 1
    if i < len(arr1):
        sol.extend(arr1[i:])
    if j < len(arr2):
        sol.extend(arr2[j:])
    return sol


def merge_sort(arr):
    """
    THe actual merge sort algorithm

    Args:
        arr (list): an unsorted list

    Returns:
        list: a sorted list

    """
    if len(arr) == 0 or len(arr) == 1:
        return arr
    start = 0
    end = len(arr)
    mid = start + (end - start) // 2
    left = merge_sort(arr[start:mid])
    right = merge_sort(arr[mid:end])
    return merge(left, right)

def check_through_arr(arr, k):
    """
    RUn through the arr to see the variables that add up to k.

    Args:
        arr (list): a sorted list
        k (int): the difference for comparison

    Returns:
        int: the count where the difference is matching

    """
    i = 0
    j = 1
    count = 0
    while j < len(arr):
        if arr[i] + k > arr[j]:
            j += 1
        elif arr[i] + k == arr[j]:
            count += 1
            i += 1
            j += 1
        else:
            i += 1

    return count


def main(arr, k):
    """ The main function"""
    arr = merge_sort(arr)
    print(arr)
    print(check_through_arr(arr, k))
    print("#"*10)

main([3, 4, 5, 12, 14, 15, 16], 2)
main([1,5,3,4,2], 2)
main([1,3, 5, 8, 6, 4, 2], 2)
