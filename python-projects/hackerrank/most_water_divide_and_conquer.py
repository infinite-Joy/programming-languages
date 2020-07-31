"""
very similar to the max subarray in CLRS book

time complexity O(n)

page 72

this is also not working out.
"""

def find_max_crossing_subarray(arr, low, mid, high):
    """
    if there is a guarantee that the max element goes through the middle
    then we can do something about it

    check the greatest water on the left
    check the greatest water on the right
    return the result

    [1,8,6,2,5,4,8,3,7]
    low = 1
    mid = 5
    high = 7
    [1,   8,  6,  2,  5,  4,  8,  3,  7]
     4    15  10  2   0   4   10  9   20
          _                           _
    """

    mostwater = 0
    maxleft = mid
    for distance, wall in enumerate(range(mid, low-1, -1)):
        possible = min(arr[mid], arr[wall])*distance
        mostwater = max(mostwater, possible)
        if mostwater == possible:
            maxleft = wall

    mostwater = 0
    maxright = mid
    for distance, wall in enumerate(range(mid, high+1)):
        possible = min(arr[mid], arr[wall])*distance
        mostwater = max(mostwater, possible)
        if mostwater == possible:
            maxright = wall

    actualwater = min(arr[maxleft], arr[maxright]) * (maxright-maxleft)
    return maxleft, maxright, actualwater


def mostwater(arr, low, high):
    if high == low + 1:
        return low, high, min(arr[high], arr[low])*1
    else:
        #__import__('pudb').set_trace()
        mid = (low + high) // 2
        leftlow, lefthigh, leftmax = mostwater(arr, low, mid)
        rightlow, righthigh, rightmax = mostwater(arr, mid, high)
        crosslow, crosshigh, crossmax = find_max_crossing_subarray(arr, low, mid, high)

        maxmax = max(leftmax, rightmax, crossmax)
        if maxmax == leftmax:
            return leftlow, lefthigh, leftmax
        if maxmax == rightmax:
            return rightlow, righthigh, rightmax
        if maxmax == crossmax:
            return crosslow, crosshigh, crossmax

arr = [1,8,6,2,5,4,8,3,7]
arr = [0, 2]
arr = [2,3,10,5,7,8,9]
print(mostwater(arr, 0, len(arr)-1))
