import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

LIMIT = 1_000_000_000

def naive(growthRates):
    users = sum([g ** (1) for g in growthRates])
    t = 1
    while users < LIMIT:
        t += 1
        users = 0
        users = sum([g ** (t) for g in growthRates])
    return t

def get_bounds(growthRates):
    left, right = 1, 2
    users = sum([g ** (right) for g in growthRates])
    while users < LIMIT:
        left = right
        right = 2*right
        users = sum([g ** (right) for g in growthRates])
    return left, right

def hone_in(growthRates, left, right):
    # print(left, right)
    while left <= right:
        # import time; time.sleep(1)
        # print(left, right)
        if left == right:
            return left
        mid = left + int((right - left) / 2)
        users = sum([g ** (mid) for g in growthRates])
        if users == LIMIT:
            return mid
        elif users < LIMIT:
            left = mid + 1
        else:
            right = mid


def getBillionUsersDay(growthRates):
    # Write your code here
    # return naive(growthRates)
    day_one_users = sum([g ** (1) for g in growthRates])
    if day_one_users > 1_000_000_000:
        return 1

    left, right = get_bounds(growthRates)
    return hone_in(growthRates, left, right)

    



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
  test_1 = [1.1, 1.2, 1.3]
  expected_1 = 79
  output_1 = getBillionUsersDay(test_1)
  check(expected_1, output_1)

  test_2 = [1.01, 1.02]
  expected_2 = 1047
  output_2 = getBillionUsersDay(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
  