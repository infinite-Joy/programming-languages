from collections import Counter
from math import fabs

def isValid(s):
    chars = Counter(s)
    print(chars)
    vals = {}
    for _, v in chars.items():
        if v not in vals:
            vals[v] = 0
        vals[v] += 1
    print(vals)
    if len(vals) == 1:
        return "YES"
    if len(vals) == 2:
        counts = list(vals.items())
        counts = sorted(counts, key=lambda x: x[1])
        if counts[0][0] - counts[1][0] not in (1, -1):
            return "NO"
        if counts[0][1] != 1:
            return "NO"
        return "YES"
    else:
        return "NO"


target = 'abcdefghhgfedecba'
print(target)
print(isValid(target))

target = 'aabbcd'
print(target)
print(isValid(target))
