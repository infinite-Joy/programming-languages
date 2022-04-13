"""

continuous subarrays

https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=226517205173943&c=1062635970997589&ppid=454615229006519&practice_plan=1

starting: Tue Apr 12 21:02:06 IST 2022

this is probably a dynamic programming problem

        3   4   1   6   2

max = 6
left    1   2   1   4   1
right   1   2   1   2   1

sol = 2 - 1
    1   3   1   5   1 so basically a dynamic programming solution

    inspired by kadanes solution


lets go ahad with a naive solution

for that elem:
    either you can only go left
    or you can only go right
    is the next one less than this then + 1
    and keep on continuing till you find the greater
    similarly for the right

complexity of this is On2

better approach:

if we can find how many digits after this digit there are descending

        3   4   1   6   2

        0   1   -1   1  -1
        0   1   0   1   0

        -1    1    -1    1    0
         0     1      0      1      0

         1  3   1
"""

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def one_way_understanding(arr):
    understanding = []
    max_el = -1
    for i, el in enumerate(arr):
        if el > arr[max_el]:
            understanding.append(i - max_el + 1)
            max_el = i




def count_subarrays(arr):
    left_understanding = one_way_understanding(arr)
    right_understanding = one_way_understanding(arr[::-1])
    right_understanding = right_understanding[::-1]
    count = [x + y - 1 for x, y in zip(left_understanding, right_understanding)]
    return count


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
  test_1 = [3, 4, 1, 6, 2]
  expected_1 = [1, 3, 1, 5, 1]
  output_1 = count_subarrays(test_1)
  check(expected_1, output_1)
  
  test_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [1, 2, 6, 1, 3, 1]
  output_2 = count_subarrays(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
