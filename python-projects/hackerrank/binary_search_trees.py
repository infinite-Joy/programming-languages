def binary_search(key, arr, left, right):
    if right < left:
        return -1
    else:
        mid = (right - left) // 2
        mid = mid + left
        if key < arr[mid]:
            right = mid
            return binary_search(key, arr, left, right)
        elif key > arr[mid]:
            left = mid
            return binary_search(key, arr, left, right)
        else:
            return mid


def search(key, arr):
    left, right = 0, len(arr)-1
    return binary_search(key, arr, left, right)


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
print(search(67, primes))
print(primes.index(67))
