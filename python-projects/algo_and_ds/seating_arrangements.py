import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

"""
 [5, 10, 6, 8]
 8  5 6 10

we can sort the arr and then start from the smallest and go to the higest


"""


def minOverallAwkwardness(arr):
    print(arr)
    # Write your code here
    if len(arr) < 3:
      return arr[0] - arr[1]
    arr.sort()
    left = [arr.pop()]
    right = [arr.pop()]
    while arr:
      if len(left) > len(right):
        right.append(arr.pop())
      elif len(right) > len(left):
        left.append(arr.pop())
      else:
        elem = arr.pop()
        print(elem, abs(left[-1] - elem), abs(right[-1] - elem))
        if abs(left[-1] - elem) >= abs(right[-1] - elem):
          left.append(elem)
        else:
          right.append(elem)
    final = left + right[::-1]
    print(final)
    val = max([abs(final[i] - final[i-1]) for i in range(len(final)-1, -1, -1)])
    return val




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
  arr_1 = [5, 10, 6, 8]
  expected_1 = 4
  output_1 = minOverallAwkwardness(arr_1)
  check(expected_1, output_1)

  arr_2 = [1, 2, 5, 3, 7]
  expected_2 = 4
  output_2 = minOverallAwkwardness(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  