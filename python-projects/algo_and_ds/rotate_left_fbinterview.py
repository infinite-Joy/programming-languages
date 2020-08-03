from copy import deepcopy


def reverse(arr, start, end):
    while end > start:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1



def rotLeft(a, d):
    # this can probably be done in O(n)
    # basically to understand where would the first element go in the array
    # and then start swapping from that number till the end with the first digit

    # [1,2,3,4,5,6,7]
    # => [3,2,3,4,5,1,7] carry 6

    # 41 73 89 7 10 1 59 58 84 77 77 97 58 1 86 58 26 10 86 51
    reverse(arr, 0, d-1)
    reverse(arr, d, len(arr)-1)
    reverse(arr, 0, len(arr)-1)
    return arr


arr = [1,2,3,4,5, 6, 7]
print(arr)
print(rotLeft(arr, 2))

arr = "41 73 89 7 10 1 59 58 84 77 77 97 58 1 86 58 26 10 86 51"
arr = arr.split()
arr2 = deepcopy(arr)
assert arr2[10:] + arr2[:10] == rotLeft(arr, 10)
