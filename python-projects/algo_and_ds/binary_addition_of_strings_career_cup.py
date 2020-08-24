"""
 facebook-interview-questions
0
of 0 votes
6
Answers

Implement binary addition of two strings.
For example "101101" and "111101" equal "1101010"
You cannot use any type conversion, operate only with strings.
"""

RULES = { '000' : '00',
            '001' : '01',
            '010' : '01',
            '011' : '10',
            '100' : '01',
            '101' : '10',
            '110' : '10',
            '111' : '11' }

def add(string1, string2):
  sol = []
  i = len(string1) - 1
  j = len(string2) - 1
  comb = '0'
  carry = '0'
  while i >= 0 and j >= 0:
    comb = carry + string1[i] + string2[j]
    carry, sum = RULES[comb]
    sol.append(sum)
    i -= 1
    j -= 1

  while i >= 0:
    comb = carry + string1[i] + '0'
    carry, sum = RULES[comb]
    sol.append(sum)
    i -= 1

  while j >= 0:
    comb = carry + "0" + string2[j]
    carry, sum = RULES[comb]
    sol.append(sum)
    j -= 1

  if carry == '1':
    sol.append(carry)
  return "".join(sol[::-1])

string1 = "101101"
string2 = "1101010"
print(add(string1, string2))
print(bin(int(string1, 2) + int(string2, 2)))
