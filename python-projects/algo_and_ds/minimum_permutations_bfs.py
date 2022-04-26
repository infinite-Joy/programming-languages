import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


"""
using the bfs to find the minimum


"""

from collections import deque


def minOperations(arr):
    # Write your code here
    target = "".join([str(x) for x in sorted(arr)])
    source = "".join([str(x) for x in arr])
    # print(source, target)
    queue = deque([(0, source)])
    visited = {source: True}
    while queue:
        level, node = queue.popleft()
        # print(node, target, level)
        if node == target:
            return level
        # get the children
        for i in range(len(node)+1):
            for j in range(i+1, len(node)+1):
                reverse = "".join(reversed(node[i:j]))
                neighbour = node[:i] + reverse + node[j:]
                if neighbour not in visited:
                    queue.append((level+1, neighbour))
                    visited[neighbour] = True
  
  
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
  n_1 = 5
  arr_1 = [1, 2, 5, 4, 3]
  expected_1 = 1
  output_1 = minOperations(arr_1)
  check(expected_1, output_1)

  n_2 = 3
  arr_2 = [3, 1, 2]
  expected_2 = 2
  output_2 = minOperations(arr_2)
  check(expected_2, output_2)
  
  # # Add your own test cases here
  