# sorted
# N < M
# output should be sorted as well
# if n ~ m
# create set out of arr1
# for elem in arr2: match with arr1set and if match yield
# time n+m
# space O(min(n, m))\

# binary search
# time nlogm -> C*N
# space O(1)

# M = N^C

# divide and conquer
# a1 = [1, 2, 3] -> [2, 4]
# a2 = [1, 3,4, 5] -> [3, 4, 5]

# a1 = [1, 1000000]
# a2 = [1, 2, ....., 1000000]
# time complexity O(logm + n+m)

# check the range of arr1 => O(1)
# if m > n*2
# search for start in arr2 => logm
# search for end in arr2 => logm
# find_duplicates(arr1, arr2start, arr2end) n+m -> N^C

def find_duplicates(arr1, arr2):
  hashset = set()

  # take the smaller one
  if len(arr1) > len(arr2):
    arr1, arr2 = arr2, arr1

  # create the hashset
  for elem in arr1:
    hashset.add(elem)

  # check for dups
  dups = []
  for elem in arr2:
    if elem in hashset:
      dups.append(elem)
  return dups

def binary_search(arr, elem, low, high):
  if high == low:
    return arr[low] == elem
  mid = (low+high) // 2
  if arr[mid] >= elem:
    return binary_search(arr, elem, low, mid)
  else:
    return binary_search(arr, elem, mid+1, high)

def find_duplicates(arr1, arr2):
  # take the smaller one
  if len(arr1) > len(arr2):
    arr1, arr2 = arr2, arr1

  dups = []
  for elem in arr1:
    if binary_search(arr2, elem, 0, len(arr2)-1):
      dups.append(elem)
  return dups


def find_duplicates(arr1, arr2):
  # two pointer method
  i = 0
  j = 0
  dups = []
  while i < len(arr1) and j < len(arr2):
    if arr1[i] == arr2[j]:
      dups.append(arr1[i])
      i += 1
      j += 1
    elif arr1[i] > arr2[j]:
      j += 1
    else:
      i += 1
  return dups


print(find_duplicates([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20]))
print(find_duplicates([], []))
print(find_duplicates([], [1,2,3]))
