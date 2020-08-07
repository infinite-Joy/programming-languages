#!/bin/python3

import math
import os
import random
import re
import sys

# this is the longest common subsequence problem



# Complete the commonChild function below.
# this looks to me like a dp problem.
# lets see if this works out
#     H   A   R   R   Y
#     0   0   0   0   0
# S   0   0   0   0   0
# A   0   1   1   1   1
# L   0   1   1   1   1
# L   0   1   1   1   1
# y   0   1   1   1   2


#     S   H   I   N   C   H   A   N
# N   0   0   0   1   0   0   0   1
# O   0   0   0   1   0   0   0   1
# H   0   1   1   1   1   2   0   1
# A   0   1   1   1   1   2   3   1
# R   0   1   1   1   1   2   3   1
# A   0   1   1   1   1   2   3   1
# A   0   1   1   1   1   2   3   1
# A   0   1   1   1   1   2   3   1


#     A   B   C   D   E   F
# F   0   0   0   0   0   1
# B   0   1   0   0   0   1
# D   0   1   0   1   0   1
# A   1   1   0   1   0   1
# M   1   1   0   1   2   2
# N   1   1   1   2   2   2

def commonChild(s1, s2):
    dp = [0 for _ in range(len(s2)+1)]
    for i1, item1 in enumerate(s1):
        for i2 in range(len(s2), 0, -1):
            if item1 == s2[i2-1]:
                dp[i2] = dp[i2-1] + 1
            else:
                dp[i2] = max(dp[i2-1], dp[i2])
    return max(dp)


def commonChild(s1, s2):
    #print([x for x in s2])
    dp = [0 for _ in range(len(s2)+1)]
    for i1, item1 in enumerate(s1):
        for i2 in range(len(s2), 0, -1):
            if item1 == s2[i2-1]:
                dp[i2] = dp[i2-1] + 1
            else:
                dp[i2] = max(dp[i2-1], dp[i2])
        #print(item1, dp)
    return max(dp)


def commonChild(s1, s2):
    #print([x for x in s2])
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for row, item1 in enumerate(s1, 1):
        for col, item2 in enumerate(s2, 1):
            if item1 == item2:
                dp[row][col] = dp[row-1][col-1] + 1
            else:
                dp[row][col] = max(dp[row-1][col], dp[row][col-1])
    for item in dp:
        print(item)
    return dp[-1][-1]

print(commonChild("HARRY", "SALLY"))
print(commonChild("AA", "BB"))
print(commonChild("SHINCHAN", "NOHARAAA"))
print(commonChild("ABCDEF", "FBDAMN"))
print(commonChild("WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS", "FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC"))


print()
print()
print("now recursion code")
def lcs(string1, string2, i, j):
    if string1[i] == "ø" or string2[j] == "ø":
        return 0
    elif string1[i] == string2[j]:
        return 1 + lcs(string1, string2, i+1, j+1)
    else:
        return max(lcs(string1, string2, i+1, j), lcs(string1, string2, i, j+1))


def main(string1, string2):
    string1 = string1 + "ø"
    string2 = string2 + "ø"
    return lcs(string1, string2, 0, 0)

print(main("HARRY", "SALLY"))
print(main("AA", "BB"))
print(main("SHINCHAN", "NOHARAAA"))
print(main("ABCDEF", "FBDAMN"))
print(main("WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS", "FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC"))
