def bst(arr, low, high):
  #print(arr, low, high)
  if low > high:
    return -1
  if high == low + 1:
    if low == arr[low]:
      return low
    if high == arr[high]:
      return high
    else:
      return -1
  mid = (high - low) // 2 + low
  #print(mid)
  curr_val = arr[mid]
  if curr_val == mid:
    return mid
  if curr_val < mid:
    low = mid
    return bst(arr, low, high)
  else:
    high = mid
    return bst(arr, low, high)


def index_equals_value_search(arr):
  # A = [-8,0,2,5]
  #           ^ => INDEX 2
  # INDEX I THAT IS EQUAL TO A[I]

  # [-8, 0, 2, 5]
  #         i

  """
  [-1,0,3,6]
          i

  # middle = len(arr)/2

  ex1 [-8, 0, 1, 3, 4, 5]
              i=2
                 i=3
    if val < i
      i should go to the right


  ex2 [0, 1, 3, 4, 6, 7]
             i=2
          i=1

  if val > i
    i should go to the left

    O lg n

  """

  low = 0
  high = len(arr)
  return bst(arr, low, high-1)

print(index_equals_value_search([-8,0,2,5]))
print(index_equals_value_search([-1,0,3,6]))
print(index_equals_value_search([-1,0,3,6, 9]))
