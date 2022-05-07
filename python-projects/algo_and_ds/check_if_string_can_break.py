"""

string can break if x[i] > y[i]

I can take a greedy approach saying that if they are sorted then the last of x will be the last of y

why this works. lets say x[n] < y[n], then it will not be the case that x[n-p] < y[n-p] after shifting. shifting will not work

"""

def check_helper(str1, str2):
    return all(x >= y for x, y in zip(str1, str2))

def check(str1, str2):
    str1 = sorted(str1)
    str2 = sorted(str2)
    if check_helper(str1, str2) or check_helper(str2, str1):
        return True
    else:
        return False

print(check('abe', 'acd'))

# ==============================================

"""
there are only 26 alphabets.
hence we can do sorting
"""

import string

def sort(s):
    chars = string.ascii_lowercase
    mapping = {ch: i for i, ch in enumerate(chars)}
    counts = [0] * len(chars)
    for ch in s:
        counts[mapping[ch]] += 1
    sorted = []
    for i, c in enumerate(counts):
        ch = chars[i]
        val = ch * c
        sorted.append(val)
    sorted = sorted[::-1]
    return "".join(sorted)

def check(str1, str2):
    str1 = sort(str1)
    str2 = sort(str2)
    if check_helper(str1, str2) or check_helper(str2, str1):
        return True
    else:
        return False

print(check('abe', 'acd'))

s1 = "leetcodee"
s2 = "interview"
print(s1, s2, check(s1, s2))