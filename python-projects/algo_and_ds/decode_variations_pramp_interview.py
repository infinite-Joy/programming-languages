def decodeVariations(S):

  string = S

  if not string:
    return 0
  if len(string) == 1 and string == '0':
    return 0

  # handling the case of 0
  for i in range(1, len(string)):
      if string[i] == '0' and string[i-1] > '2':
          return 0

  zero = 1
  if string[0] == '0':
    one = 0
  else:
    one = 1
  curr = one # this is just a random value   1

  for i in range(1, len(string)):
    # i can combine with previous
    if 1 <= int(string[i-1] + string[i]) <= 26:
      curr = zero + one
    else:
      if string[i] == '0':
        curr = zero
      else:
        curr = one

    zero = one
    one = curr

  return curr

#print(decodeVariations('1262'))
print(decodeVariations('1270'))
print(decodeVariations('83778549129'))


"""

  1   2   6   2

  0 => 0
  1 => 1
  1 2 => 1:2, 12 => 2
  126 => 1:2:6, 12:6, 1:26 => 3
  1262 => 1262, 1:26:2, 12:6:2 => 3
  12621 => 1:2:6:2:1, 1:26:2:1, 12:6:2:1, 1:2:6:21, 1:26:21, 12:6:21  => 6


  dp[i] = dp[i-1] + 1 if i can combine
        else dp[i-1]

  if number is empty: return 0
  if numver is 0 and there is only 1 digit: return 0

  time: O(n)
  space: O(1)

"""


