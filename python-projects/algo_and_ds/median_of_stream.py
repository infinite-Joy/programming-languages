"""
calculating the median of a stream of values.

https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=547645422524434&c=1062635970997589&ppid=454615229006519&practice_plan=0

we can create two heaps, one is the min heap and the max heap. min heap for big half

and the max heap for the smaller half

the complexity of this operation is O(nlogn) while the percentage of getting each of the entries is O(1)

https://stackoverflow.com/questions/10657503/find-running-median-from-a-stream-of-integers

"""

from heapq import heappush, heappop, heapify, heapreplace

class Median:
    def __init__(self):
        self.left = []
        self.right = []
        
    def get_median(self):
        # print(self.left, self.right)
        if len(self.left) == len(self.right):
            return (-1 * self.left[0] + self.right[0]) / 2
        elif len(self.left) > len(self.right):
            return -1 * self.left[0]
        else:
            return self.right[0]

    def insert_first_time(self, val):
        if not (self.left or self.right):
            self.left.append(-val)
            return True

    def heapify(self, arr, val):
        if not arr:
            arr.append(val)
        else:
            heappush(arr, val)

    def insert(self, val):
        # for the first case
        if self.insert_first_time(val):
            return

        # if val more than right min
        # if length is same then push right.
        # if left length is more then its fine. push right
        # if right length is more then push right, extract min elem and then push left
        if self.right and val > self.right[0]:
            if len(self.left) >= len(self.right):
                self.heapify(self.right, val)
            else:
                heappush(self.right, val)
                val = heappop(self.right)
                heappush(self.left, -val)

        # if val is less than equal left max. # this is same as less than right min
        # if length is same then push left.
        # if right length is more than its fine push right.
        # if the left length is more than push left, extract max and then push right
        else:
            if len(self.right) >= len(self.left):
                self.heapify(self.left, -val)
            else:
                heappush(self.left, -val)
                val = heappop(self.left)
                heappush(self.right, -val)

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def findMedian(arr):
    # print(arr)
    m = Median()
    medians = []
    for elem in arr:
        m.insert(elem)
        medians.append(m.get_median())
    return medians
  



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
  arr_1 = [5, 15, 1, 3]
  expected_1 = [5, 10, 5, 4]
  output_1 = findMedian(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [2, 3, 4, 3, 4, 3.5]
  output_2 = findMedian(arr_2)
  check(expected_2, output_2)


  # Add your own test cases here
  