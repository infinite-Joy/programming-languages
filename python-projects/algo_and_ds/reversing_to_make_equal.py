"""
https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=2869293499822992&c=1062635970997589&ppid=454615229006519&practice_plan=0

first is a simple check. if any number is there is any digit that are not in one or the other then we can just make this false.

we can probably think of a tree like structure for this.

"""


import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def are_they_equal(array_a, array_b):
  # Write your code here
  mapping = {}
  for item in array_a:
      if item in mapping:
          mapping[item] += 1
      else:
          mapping[item] = 1

  for item in array_b:
      if item in mapping:
          mapping[item] -= 1
      else:
          return False
  return not any(x!=0 for x in mapping.values())
        
  










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
  n_1 = 4
  a_1 = [1, 2, 3, 4]
  b_1 = [1, 4, 3, 2]
  expected_1 = True
  output_1 = are_they_equal(a_1, b_1)
  check(expected_1, output_1)

  n_2 = 4
  a_2 = [1, 2, 3, 4]
  b_2 = [1, 2, 3, 5]  
  expected_2 = False
  output_2 = are_they_equal(a_2, b_2)
  check(expected_2, output_2)

  # Add your own test cases here
  n_3 = 5
  a_3 = [1, 2, 3, 4, 5]
  b_3 = [3, 1, 2, 5, 4]  
  expected_2 = False
  output_2 = are_they_equal(a_2, b_2)
  check(expected_2, output_2)