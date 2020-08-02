from math import factorial

MOD = 10**9 + 7

n, k = map(int, input().split(' '))
a = [int(input()) for _ in range(n)]

bit = 1 << 59
val = 0
while bit:
    b = [x for x in a if x & bit]
    if len(b) >= k:
        val |= bit
        a = b
    bit >>= 1

n = len(a)
print(val)
print(factorial(n) // factorial(k) // factorial(n - k) % MOD)
