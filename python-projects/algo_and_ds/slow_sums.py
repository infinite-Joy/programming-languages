import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

"""
4 + 3
4 + 3 + 2
4 + 3 + 2 + 1
so the bottleneck is sorting. need to find a way to do this without sorting.

"""




def getTotalTime(arr):
  # Write your code here
  arr.sort()
  max_penalty = 0
  for i in range(len(arr)-1):
    max_penalty += arr[i] * (i + 1)
    print(max_penalty)
  max_penalty += arr[-1] * (i+1)
  return max_penalty
  


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [4, 2, 1, 3]
  expected_1 = 26
  output_1 = getTotalTime(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 3, 9, 8, 4]
  expected_2 = 88
  output_2 = getTotalTime(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  