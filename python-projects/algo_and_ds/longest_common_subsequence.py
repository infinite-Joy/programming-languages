"""

longgest commoon subsequence

using recursion and memorisation and tabulation

"""


def lcs(s1, s2, i, j, memo=None):
    memo = {} if memo is None else memo
    if (i, j) in memo: return memo[(i, j)]

    if i >= len(s1) or j >= len(s2):
        return 0
    elif s1[i] == s2[j]:
        memo[(i, j)] = 1 + lcs(s1, s2, i+1, j+1)
        return memo[(i, j)]
    else:
        memo[(i, j)] = max(lcs(s1, s2, i+1, j), lcs(s1, s2, i, j+1))
        return memo[(i, j)]

S1 = 'bcdaacd'
S2 = 'acdbac'

print(lcs(S1, S2, 0, 0))