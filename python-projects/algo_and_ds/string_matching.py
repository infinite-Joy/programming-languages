def brute_force(fulltext, pattern):
    for i in range(len(fulltext) - len(pattern) + 1):
        j = 0
        matchedtillnow = True
        #print(i)
        while matchedtillnow is True and j < len(pattern):
            #print(fulltext[i+j], pattern[j], fulltext[i+j] == pattern[j])
            matchedtillnow = fulltext[i+j] == pattern[j]
            j += 1
        if matchedtillnow is True:
            return True
    return False

print(brute_force("ababababababa", "bab"))
print(brute_force("aaab", "ab"))
print(brute_force("aldgfahfkj", "xxx"))


from functools import lru_cache
from collections import deque


def rollinghash(nextch, curr_rolling_hash, queue, d, k):
    d_size = len(d) # 4
    outgoing = queue.popleft() #
    queue.append(nextch)
    val = curr_rolling_hash - (d[outgoing] * (d_size**(k-1)))
    val = val * d_size
    return val + d[nextch]

test_queue = deque(["a", "b", "c"])
print("rollinghash", rollinghash("d", 27, test_queue, {'a':1, 'b':2, 'c':3, 'd':4}, 3))
print('test queue after change', test_queue)


def hashfunction(queue, d, k):
    size = len(d)
    hash_val = [d[x] * size**(k-1-i) for i, x in enumerate(queue)]
    return sum(hash_val)

print(hashfunction(['a', 'b', 'c'], {'a':1, 'b':2, 'c':3, 'd': 4},3))


def check_values(fulltext, pattern, i):
    n = len(pattern) - 1
    for j in range(n+1):
        if pattern[n-j] != fulltext[i-j]:
            return False
    return True


print(check_values("abc", "abc", 2))
print(check_values("abc", "abd", 2))


def rabin_karp(fulltext, pattern):
    d = {k: v for v, k in enumerate(set(list(fulltext)))}
    queue = deque([])

    pattern_size = len(pattern)
    patternhash = hashfunction(pattern, d, pattern_size)

    for i, ch in enumerate(fulltext):
        curr_rolling_hash = 0
        if i < len(pattern) - 1:
            queue.append(ch)
        elif i == len(pattern) - 1:
            curr_rolling_hash = hashfunction(queue, d, pattern_size)
        else:
            curr_rolling_hash = rollinghash(ch, curr_rolling_hash, queue, d, pattern_size)

        if curr_rolling_hash == patternhash:
            # do the actual  check
            if check_values(fulltext, pattern, i) is True:
                return i - pattern_size

    return False


print(rabin_karp("ababababababa", "bab"))
print(rabin_karp("aaab", "ab"))
print(rabin_karp("aldgfahfkj", "xxx"))
