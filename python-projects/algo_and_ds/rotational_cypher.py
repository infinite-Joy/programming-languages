"""
rotational cypher

https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=238827593802550&c=1062635970997589&ppid=454615229006519&practice_plan=1

completed in 15 mins

"""


import math
import string
# Add any extra import statements you may need here


# Add any helper functions you may need here


def rotationalCipher(input, rotation_factor):
    # Write your code here
    alphabets = string.ascii_lowercase
    numbers = string.digits
    new_alpabet = []
    for ch in input:
        case = ch.isupper()
        ch = ch.lower()
        # print(ch)
        if ch.isalpha():
            index = alphabets.index(ch)
            shift = rotation_factor % len(alphabets)
            actual_place = (index + shift) % len(alphabets)
            new_alpabet.append(alphabets[actual_place])
        elif ch.isdigit():
            index = numbers.index(ch)
            shift = rotation_factor % len(numbers)
            actual_place = (index + shift) % len(numbers)
            new_alpabet.append(numbers[actual_place])
        else:
            new_alpabet.append(ch)
        if case:
            new_alpabet[-1] = new_alpabet[-1].upper()
    return "".join(new_alpabet)


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
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)

  # Add your own test cases here
  