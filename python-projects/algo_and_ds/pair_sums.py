"""

pair sums

https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=840934449713537&c=1062635970997589&ppid=454615229006519&practice_plan=1

Wed Apr 13 00:05:10 IST 2022
Wed Apr 13 00:32:34 IST 2022

can be done using map. where the mapping is between the indices

rute force is O(n2) because for each element you will go through the array twice.

hence this can be done in O(n)

duplciates become like an edge case

"""

import math
from functools import reduce
import operator
# Add any extra import statements you may need here


# Add any helper functions you may need here

def comb(n, r):
    r = min(r, n-r)
    num = reduce(operator.mul, range(n, n-r, -1), 1)
    den = reduce(operator.mul, range(r, 1, -1), 1)
    return int(num / den)

print(comb(2, 2))


def numberOfWays(arr, k):
    # Write your code here
    map = {}
    seen = {}
    count = 0
    for i, item in enumerate(arr):
        # 5: 1, 3: 3
        diff = k - item
        if item in map:
            map[item] += 1
        else:
            if diff == item:
                map[diff] = 1
            else:
                map[diff] = 0
    print(map)
    print([comb(x, 2) for x in map.values() if x > 0])
    return sum([comb(x, 2) for x in map.values() if x > 0])
    

  












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
  k_1 = 6
  arr_1 = [1, 2, 3, 4, 3]
  expected_1 = 2
  output_1 = numberOfWays(arr_1, k_1)
  check(expected_1, output_1)

  k_2 = 6
  arr_2 = [1, 5, 3, 3, 3]
  expected_2 = 4
  output_2 = numberOfWays(arr_2, k_2)
  check(expected_2, output_2)

  # Add your own test cases here
  