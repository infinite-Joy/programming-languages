import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

"""

complexity: O(n) + O(m log(n))

"""

def search(prefix_sums, val):
    # print(prefix_sums, val)
    mid = int(len(prefix_sums) / 2)
    left = 0
    right = len(prefix_sums) - 1
    if val > prefix_sums[right]:
        return -1
    while left < right:
        # print('left, right', left, right)
        if left + 1 == right:
            return right
        mid = left + int((right - left) / 2)
        # print('left, right, mid', left, right, mid)
        if val == prefix_sums[mid]:
            return mid
        elif val < prefix_sums[mid]:
            right = mid
        else:
            left = mid


def getMilestoneDays(revenues, milestones):
    # Write your code here
    # prefix sum will have one more
    prefix_sums = [0]
    for i, item in enumerate(revenues):
        prefix_sums.append(prefix_sums[-1] + item)
    output = []
    for q in milestones:
        output.append(search(prefix_sums, q))
    return output

  

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

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
  revenues_1 = [100, 200, 300, 400, 500]
  milestones_1 = [300, 800, 1000, 1400]
  expected_1 = [2, 4, 4, 5]
  output_1 = getMilestoneDays(revenues_1, milestones_1)
  check(expected_1, output_1)

  revenues_2 = [700, 800, 600, 400, 600, 700]
  milestones_2 = [3100, 2200, 800, 2100, 1000] 
  expected_2 = [5, 4, 2, 3, 2]
  output_2 = getMilestoneDays(revenues_2, milestones_2)
  check(expected_2, output_2)

  # Add your own test cases here
  