"""

create a hash map of the abs val to the list of actual values
sort the numbers based on the tuple
if first value is conflicting, i can do normal sort
return the solution

time complexity: O(n)
space complexity: O(n)

count sort:
  find the max
  initialise from 0 to max
  put the counts of the individual numbers there
  then accumulate
  and then reverse from the end to find the actual numbers.

"""



from math import fabs
from bisect import insort

def count_sort(sol, abs_mapping):
  # [2, -7, -2, -2, 0]
  # absmapping = {2: [-2, -2, 2], 7: [-7], 0: [0]}
  # sol = [2,7,0]
  maxval = max(sol) # 7

  helper_arr = [0 for _ in range(maxval+1)]

  for item in sol:
    helper_arr[item] += 1

  # do the accumulation
  helper_arr1 = []
  val = 0
  for idx, item in enumerate( helper_arr ):
    val = val + item
    helper_arr1.append(val)
  helper_arr = helper_arr1

  # finally try to build the solution
  solution = []
  for idx in range(len(helper_arr)-1, 0, -1):
    if helper_arr[idx] != helper_arr[idx-1]:
      solution.extend(reversed(abs_mapping[idx]))
  if helper_arr[0] > 0:
    solution.extend(abs_mapping[0])

  return solution[::-1]


def absSort(arr):
  abs_mapping = {}
  sol = set()
  for num in arr:
    abs_num = int(fabs(num))
    if abs_num not in abs_mapping:
      abs_mapping[abs_num] = [num]
    else:
      # insert into the arr in sorted manner
      insort(abs_mapping[abs_num], num)

    sol.add(abs_num)
  return count_sort(list(sol), abs_mapping)

# test cases
arr = [2, -7, -2, -2, 0]
print(absSort(arr))
