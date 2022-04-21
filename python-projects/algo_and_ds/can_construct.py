"""

write a function that can accepts a target sting and can construct from a list of substrings.

this can be done using dynamic programming

reference: https://www.youtube.com/watch?v=oBt53YbR9Kk&t=7077s

brute force:
    target: n
    words: m
    time: O(n^m * n)
    space: O(n)

"""

import random
import string


def can_construct(target, words):
    # print(target, words)
    if target == '':
        return True

    for w in words:
        if target.startswith(w) or target.endswith(w):
            # print(w)
            if can_construct(target.replace(w, ''), words):
                return True
        elif w in target:
            res = True
            for children in target.split(w):
                # print(w, children)
                res = res and can_construct(children, words)
            if res is True:
                return True
        else:
            pass
    return False

def can_construct_dp(target, words, memo=None):
    memo = {} if memo is None else memo
    # print(target, words)
    if target in memo:
        memo['count'] += 1
        return memo[target]
    if target == '':
        return True

    for w in words:
        if target.startswith(w):
            # print(w)
            if can_construct_dp(target.replace(w, ''), words, memo):
                memo[target] = True
                return True
        # elif w in target:
        #     res = True
        #     for children in target.split(w):
        #         # print(w, children)
        #         res = res and can_construct_dp(children, words, memo)
        #     if res is True:
        #         memo[target] = True
        #         return True
        else:
            pass
    memo[target] = False
    return False

print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'board']))


 
def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

chars = string.ascii_letters.lower()
size = 100000000

import time
st = time.time()
# print(can_construct(random_string_generator(size, chars), ['bo', 'rd', 'ate', 't', 'ska', 'board']), time.time()-st)
memo = {'count': 0}
print(can_construct_dp(random_string_generator(size, chars), ['bo', 'rd', 'ate', 't', 'ska', 'board'], memo), time.time()-st)
print(memo['count'])
