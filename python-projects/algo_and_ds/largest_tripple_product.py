"""
;largest tripple product

https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=510655302929581&c=1062635970997589&ppid=454615229006519&practice_plan=0

build the max heap and then keep track of the 


"""

import math
from heapq import heappop, heappush, heapreplace
from functools import reduce
# Add any extra import statements you may need here


# Add any helper functions you may need here

# probably replacing the minimum elem would be the best thing


def findMaxProduct(arr):
    # print(arr)
    # Write your code here
    # for max heap need to do the reverse of the elem
    heap = []
    products = []
    running_product = 1
    count = 0
    for elem in arr:
        running_product = abs(running_product * elem)
        if count == 0:
            heap.append(elem)
            products.append(-1)
            count += 1
        elif count < 2:
            heappush(heap, elem)
            products.append(-1)
            count += 1
        elif count == 2:
            heappush(heap, elem)
            products.append(running_product)
            count += 1
        else:
            min_elem = heap[0]
            if elem > min_elem:
                going_out = heapreplace(heap, elem)
            else:
                going_out = elem
            # print(heap, going_out)
            running_product = running_product / going_out
            products.append(running_product)
    return products



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
  arr_1 = [1, 2, 3, 4, 5]
  expected_1 = [-1, -1, 6, 24, 60]
  output_1 = findMaxProduct(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [-1, -1, 56, 56, 140, 140]
  output_2 = findMaxProduct(arr_2)
  check(expected_2, output_2)


  # Add your own test cases here
  