"""
https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=2237975393164055&c=1062635970997589&ppid=454615229006519&practice_plan=0

s = "dcbefebce"
t = "fd"
output = 5

find the left most letter.
find the right most letter
that is the length of the arr


left most letter is d
right most letter is f

create the hashmap of the letters in s with the index
loop over t. and get the minimum and max letter.
max - min is the answer.

for each element.
    get the minimum of all the other elements.
        check the maximum that of those elements.

naive solution:


two pointers


thinking of the solutions
1. naive brute force
2. bottlenecks, unnecessary work, duplicated work
3. work on a related simpler problem
4. make the problem statement smaller
5. visualise the larger problem
6. test your solution on a few examples.

algo

initialise left and right



"""

import math
from collections import Counter
# Add any extra import statements you may need here


# Add any helper functions you may need here


def get_violation(req, curr, done):
    if len(done) == len(req):
        return True
    for k, v in req.items():
        if curr.get(k, 0) < v:
            return False
        else:
            done[k] = True
    return True

def min_length_substring(s, t):
    """
    s1 = "dcbefebce"
    t1 = "fd"
    """
    left = 0
    right = 0
    req = Counter(t) # {f:1, d:1}
    curr = {}
    # violations = {k: v for k, v in req.items()} # take a copy of the requests
    min_length = math.inf
    done = {} # for making sure that we are not checking for the same elements again and again
    for right in range(len(s)): # d, c
        # print(curr)
        in_ch = s[right] # d, c
        if in_ch not in curr:
            curr[in_ch] = 0 
        curr[in_ch] += 1 # {d:1, c:1}
        while left < right + 1 and get_violation(req, curr, done): # doing this again and again. can optimise this.
            min_length = min(min_length, right - left + 1)
            out_ch = s[left]
            curr[out_ch] -= 1
            if out_ch in req and curr.get(out_ch, 0) < req.get(out_ch, 0):
                del done[out_ch]
            left += 1
    return min_length if min_length != math.inf else -1


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
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  # Add your own test cases here
  