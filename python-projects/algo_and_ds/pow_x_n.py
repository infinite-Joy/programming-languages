"""

https://leetcode.com/problems/powx-n/

find x ** n

Mon Apr 11 09:18:23 IST 2022

simple solution: do the multiplication n times.

better solution probably is to 23 * 23

16 * 2 = 10 * 2 + 6 * 2 = 20 + 12

using a map that can be found.

using memoisation
"""

import math
from functools import reduce, lru_cache
import operator
import timeit

def naive_solution(x, n):
    return reduce(operator.mul, [x]*n, 1)

def inhouse(x, n):
    return x**n



def break_num(n):
    exp = 10
    digits = []
    while n:
        rem = n % exp
        n -= rem
        n = int(n / exp)
        digits.append(rem)
    return digits # least significant first

@lru_cache
def mul_ind(n1, n2):
    return n1 * n2


def multiply(n1, n2):
    list_nums = break_num(n1)
    exp = 1
    product = 0
    for num in list_nums:
        p = mul_ind(num, n2)
        p = p * exp
        exp = exp * 10
        product += p
    return product


def sol_v2(x, n):
    if n == 0:
        return 1

    if n == 1:
        return x

    curr = x
    for pow in range(2, n+1):
        curr = multiply(curr, pow)

    return curr



# print(timeit.timeit(lambda: naive_solution(91, 1000), number=10000))
# print(timeit.timeit(lambda: inhouse(91, 1000), number=10000))

# print(sol_v2(3, 6))
# print(729 * 6)
# assert sol_v2(3, 6) == 3 ** 6, (sol_v2(3, 6), 3**6)


#############################################################################

"""
THis was confusing to me but this is basically a divide and conquer approach

basically do a recursion and then on the output do a multiplication and then return the result.

2** 10 = 2 ** 5 * 2 ** 5

2 ** 5 = 2 ** 2 * 2 ** 2 * 2
"""

def sol_v3(x, n):
    if n == 1:
        return x
    if n == 0:
        return 1
    if x == 0:
        return 0

    brokenpow = sol_v3(x, n//2)
    rem = n - 2 * int(n/2)
    rem = sol_v3(x, rem)
    total = brokenpow * brokenpow * rem
    return total

def main(x, n):
    if n >= 0:
        return sol_v3(x, n)
    return 1 / sol_v3(x, abs(n))

print(sol_v3(2, 10))
print(main(2, -2))