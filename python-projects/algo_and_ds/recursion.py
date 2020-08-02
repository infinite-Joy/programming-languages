def good_fibonacci(n):
    if n <= 1:
        return (n,0)
    else:
        (a, b) = good_fibonacci(n - 1)
        return (a+b, a)

print(good_fibonacci(5))

def find_max(S, n, c_max=0):
    c_max = max(c_max, S[n])
    if n == 0:
        return c_max
    else:
        return find_max(S, n-1, c_max)


def find_max(S, c_max=0):
    try:
        S_n = next(S)
        c_max = max(c_max, S_n)
        return find_max(S, c_max)
    except StopIteration:
        return c_max


def find_max_pub(S):
    iter_S = iter(S)
    n = len(S)
    return find_max(iter_S, n-1)

print(find_max_pub([5,4,3,2,1]))


def check_palindrome(S):
    if len(S) == 0:
        return True
    elif len(S) == 1:
        return True
    else:
        first, last = S[0], S[-1]
        if first == last:
            return check_palindrome(S[1:-1])
        else:
            return False


print(check_palindrome('racecar'))
print(check_palindrome('gohangasalamiimalasagnahog'))
print(check_palindrome('abc'))


# sherlock and the valid string
#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import defaultdict

def check_discrepency(val, curr_max, lifeguard, last):
    if val < curr_max:
        if last:
            return False, False
        return lifeguard, True
    if val==curr_max:
        return lifeguard, True
    elif lifeguard and val == curr_max + 1:
        return False, True
    elif lifeguard is False and val == curr_max + 1:
        return False, False
    else:
        return False, False

def is_invalid(current_counts, curr_max, last=False):
    lifeguard = True
    for k, v in current_counts.items():
        lifeguard, ok = check_discrepency(v, curr_max, lifeguard, last)
        #print(lifeguard, ok, k, v, curr_max, lifeguard)
        if ok is False:
            return True


#print(is_invalid({'a': 1, 'b': 1, 'c': 1, 'd': 2, 'e': 3, 'f': 2, 'g': 2, 'h': 2}, 2))

def build_counter(N, S, current_counts=None, curr_max=0):
    if current_counts is None:
        current_counts = defaultdict(int)
    if len(S) == 0:
        if is_invalid(current_counts, curr_max, last=True):
            return "NO"
        else:
            return "YES"
    letter = S[0]
    current_counts[letter] += 1
    curr_max = int(N / len(current_counts))
    #print(S, current_counts, curr_max)
    if is_invalid(current_counts, curr_max):
        return "NO"
    return build_counter(N, S[1:], current_counts, curr_max)


def is_valid(S):
    N = len(S)
    return build_counter(N, S)


print(is_valid("abc"))
print(is_valid("abcc"))
print(is_valid("abccc"))
print(is_valid("aabbcd"))
print(is_valid("abcdefghhgfedecba"))
print(is_valid("aabbc"))
print(is_valid("abbccc"))


