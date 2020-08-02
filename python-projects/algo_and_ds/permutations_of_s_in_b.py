s = "xacxzaa"
b = "fxaazxacaaxzoecazxaxaz"

from itertools import permutations

def solution(s, b):
    count = 0
    for perm in permutations(s, len(s)):
        comb = "".join(perm)
        if comb in b:
            count += 1
            yield comb
    yield count

for sol in solution(s, b):
    print(sol)

print("%"*20)

def combination(sofar, rest):
    if rest == "":
        yield sofar
    else:
        for i, nextch in enumerate(rest):
            nextch = sofar + nextch
            remaining = rest[:i] + rest[i+1:]
            yield from combination(nextch, remaining)


def matching(s, b):
    count = 0
    seen = {}
    for perm in combination("", s):
        if perm in b:
            if perm not in seen:
                seen[perm] = True
                count += 1
                yield perm
    yield count

for c in matching(s, b):
    print(c)


print("#"*20)

from collections import Counter

def solution3(s, b):
    total_size = len(s)
    ch_counts = Counter(s)
    for i in range(len(b) - len(s)):
        if b[i] in ch_counts:
            curr_word = b[i:i+total_size]
            this_counts = Counter(curr_word)
            if len(this_counts) == len(ch_counts):
                matching = all([ch_counts[x]==this_counts[x] for x in ch_counts.keys()])
                if matching is True:
                    yield curr_word

for c in solution3(s, b):
    print(c)

