"""

  1  c   r   i   m   e
     99 114 	105 	109 	101
     run an accumulation
     100 	214 	319 	428 	529
     -26  -26

          netween ord(a) and ord(z)

decrypt:

    d 	n 	o 	t 	q
    convert them to the ascii values
    100 110
    +26 10
        36
        62
        88
        114

edge cases:
  null => null
  one value => do -1

decrypt('a') => 'z'

1. have a solution arr
2. for letters in the arr:
      subtract the previous value from this number
      check if adding 26 is within bound and keep going ahead
      once we reach the bound then add the element to the solution arr
      for this pos, add the previous value back

time complexity: O(n)
space complexity: O(1)

"""

def decrypt(word):
  ub = ord('z')
  solution = []
  ords = 1
  for letter in word:
    num = ord(letter)
    num -= ords
    while num + 26 <= ub:
      num += 26
    solution.append(chr(num))
    ords = num + ords
  return "".join(solution)

word = "dnotq"
print(decrypt(word))

word = 'a'
print(decrypt(word))

word = "flgxswdliefy"
print(decrypt(word))

