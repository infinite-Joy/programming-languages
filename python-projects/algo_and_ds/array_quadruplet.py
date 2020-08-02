"""
Question tried on pramp

time complexity O(n3)
space complexity O(1)
"""


def combinations(arr):
  for i, item1 in enumerate(arr):
    for j, item2 in enumerate(arr):
      if i != j:
        yield (i, item1, j, item2)


def find_matching_pair(arr, i, j, s, m, n):
  if m >= n:
    return None, None
  if arr[m] + arr[n] == s:
    return arr[m], arr[n]
  elif arr[m] + arr[n] > s:
    return find_matching_pair(arr, i, j, s, m, n-1)
  elif arr[m] + arr[n] < s:
    return find_matching_pair(arr, i, j, s, m+1, n)

"""
[0,1,2,3,4,5,7,9]
 i j j1         end
 i       j      end
16

1, 9
"""



def algo(arr, s):
  for i, num1, j, num2 in combinations(arr):
    rem = s - num1 - num2 # 16
    others1, others2 = find_matching_pair(arr, i, j, rem, m=j+1, n=len(arr)-1)
    if others1 is not None and others2 is not None:
      return [num1, num2, others1, others2]
  else:
    return []


def find_array_quadruplet(arr, s):
  arr.sort()
  return algo(arr, s)

print(find_array_quadruplet([4,4,4,4], 16))
arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 20
print(find_array_quadruplet(arr, s))










"""
[2, 7, 4, 0, 9, 5, 1, 3]

[0,1,2,3,4,5,7,9]

  0, 4 , 7 => 9 . logn
  n3logn

  0, 4 => 16 => n2, n => n3

"""

