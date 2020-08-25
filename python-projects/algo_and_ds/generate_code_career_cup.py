# https://www.careercup.com/question?id=19300678
"""
input: 1123

this is something like an n2 solution

dp[0] = [1]
dp[1] = dp[0]*1 + dp[-1]*11 = 1*1 + 11
dp[2] = dp[1]*2 + dp[0]*12 = 1*1*2 + 11*2 + 1*12
dp[3] = dp[]

time complexity: O(n2)
space complexity: O(n2)


"""

from string import ascii_letters
from typing import List

delemiter = ':'

def generate_substrings(number: str) -> List[str]:
    # time complexity O(n2)
    # space complexity O(n2)

    # generate numbers from 1 to 26 as that is the range of the english alphabet
    valid = [str(num) for num in range(1, 27)]

    # if there are no values in the number or the number of values is only 1
    if len(number) in (0, 1):
        return [number]

    # the base cases for the dp, similar to fibonacci
    # taking an example of "123"
    one = [number[0]] # 1
    two = [number[0] + delemiter + number[1], number[:2]] # [1:2, 12]

    for idx in range(2, len(number)):
        item = number[idx] # 3
        prev_chr = number[idx-1] # 2
        current = [comb + delemiter + item for comb in two] # [1:2:3, 12:3]
        possible_twos = prev_chr + item # 23
        if possible_twos in valid:
            current.extend([comb + delemiter + possible_twos for comb in one]) # [1:2:3, 12:3,     1:23]
        one = two
        two = current
    return current

def generate_codes(number):
    combinations = generate_substrings(number) # [1:2:3, 12:3, 1:23]
    sol = []
    for comb in combinations:
        temp = []
        for num in comb.split(delemiter):
            ch = ascii_letters[int(num)-1] # 1:2:3
            temp.append(ch) # a,b,c
        sol.append("".join(temp)) # ["abc"]
    return sol

print(generate_codes("1123"))
