def find_pivot(arr):
  low = 0
  high = len(arr) - 1
  while low < high:
    if low + 1 == high:
      if arr[low] > arr[high]:
        return low
      else:
        return len(arr) - 1
    mid = (low + high) // 2
    if arr[mid] > arr[low]:
      low = mid
    else:
      high = mid

def binary_search(arr, target, low, high):
  while low < high;
    mid = (low + high) // 2
    if target > arr[mid]:
      low = mid + 1
    else:
      high = mid
  return low


def find_number(arr, pivot):
  if pivot == len(arr) - 1:
    low = 0
    high = pivot
  leftmin = arr[0]
  leftmax = arr[pivot]
  if leftmin <= target <= leftmax:
    return binary_search(arr, target, 0, pivot + 1)
  else:
    return binary_search(arr, target, pivot + 1, len(arr))


"""
    1. i have the pivot from the first part
  2. either the pivot is somewhere in the middle or it is at the end
  3. if it is at the end, low = 0, high = pivot
  4. if it is somewhere in the middle.
      left min = value at 0
      left max = value at pivot

      if target withing left min and max: then low = 0 and high = pivot
      else: low = pivot + 1 and high = last

    lastly if i dont find it i return -1
"""




def shifted_arr_search(shiftArr, num):
  p = find_pivot(arr)
  return find_number(arr, pivot)



"""

brute force:
  search through the arr and find the index

  time complexity: linear
  space: constant

second approach:

  1. find pivot using bs, time complexity
  2. do a binary search on the left or the right of the pivot

  regarding 1:

    low and high are the bounding pointers
    if low + 1 == high:
      if low > high
        return low (breaking cond)
      else:
        we are guaranteed that the shifting did not happend
        return len(arr) - 1
    get the half
    check if mid is more than low:
      update my low to mid
    else
      update my high to mid

    =============

    low and high are the bounding pointers
    if low + 1 == high
      if low value > high value: return low pointer
      else return None
    get the half
    implement 2 recurions
      low, mid
      mid + 1, high
      return low or high

  2   4   5   9   12    17i
                   l     h


  [5, 9, 12, 17, 2, 4]
             l   h

   [5, 9, 12, 17, 2, 3, 4]
              _


Moving on with the second part

  1. i have the pivot from the first part
  2. either the pivot is somewhere in the middle or it is at the end
  3. if it is at the end, low = 0, high = pivot
  4. if it is somewhere in the middle.
      left min = value at 0
      left max = value at pivot

      if target withing left min and max: then low = 0 and high = pivot
      else: low = pivot + 1 and high = last

    lastly if i dont find it i return -1

time complexity : log size of the arr
space ccomplexity : constant

"""
