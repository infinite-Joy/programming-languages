import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

"""
for this sorting
do the sum of all the arraus in the aray. then keep on moving the pointer to the left  

time complexity: O(nlogn)
space complexity: O(1)

"""


def balancedSplitExists(arr):
    # Write your code here
    arr.sort()
    # print(arr)
    left_sum = 0
    right_sum = sum(arr)
    for i, elem in enumerate(arr):
        left_sum += elem
        right_sum -= elem
        # print(left_sum, right_sum)
        if left_sum < right_sum:
            pass
        elif left_sum == right_sum:
            if elem == arr[i+1]:
                return False
            else:
                return True
        else:
            return False
    return False


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [2, 1, 2, 5]
  expected_1 = True
  output_1 = balancedSplitExists(arr_1)
  check(expected_1, output_1)

  arr_2 = [3, 6, 3, 4, 4]
  expected_2 = False
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  