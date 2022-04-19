import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
"""

for any number the lexicographically smallest number would probably be the one where the smallest number can be moved to the highest place.


1 2 3 4 5

first find the min element

left side of the min element
right side of the minimum element

if k is still greater than 0 repeat the process


"""

def find_minimum(arr, k):
  min_el = arr[0]
  min_idx = 0
  for i, el in enumerate(arr[:k+1]):
    min_el = min(el, min_el)
    if min_el == el:
      min_idx = i
  return min_el, min_idx
     

def findMinArray(arr, k):
    # Write your code here
    min_el, min_idx = find_minimum(arr, k)
    for i in range(min_idx, 0, -1):
      arr[i], arr[i-1] = arr[i-1], arr[i]
    rem = k - min_idx
    curr = min_idx + 1
    while rem > 0:
      arr[curr], arr[curr + 1] = arr[curr + 1], arr[curr]
      curr += 2
    return arr




# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 3
  arr_1 = [5, 3, 1]
  k_1 = 2 
  expected_1 = [1, 5, 3]
  output_1 = findMinArray(arr_1,k_1)
  check(expected_1, output_1)

  n_2 = 5
  arr_2 = [8, 9, 11, 2, 1]
  k_2 = 3
  expected_2 = [2, 8, 9, 11, 1]
  output_2 = findMinArray(arr_2,k_2)
  check(expected_2, output_2)

  # Add your own test cases here
  