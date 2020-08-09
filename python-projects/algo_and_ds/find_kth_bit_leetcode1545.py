"""
https://leetcode.com/contest/weekly-contest-201/problems/find-kth-bit-in-nth-binary-string/
S1 = "0"
Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1
0
0 1 1
011 1  001
0111001 1 0110001

time complexity : k.log(fac(k))

num = 0, size = 1
k = 2, num << size + 1 + 1 <1 + , size = size*2 + 1 = 3
k = 3, num << size +1 + 1 << size + (~num), size = size * 2 + 1 = 7
finally once full k is reached. find the nth bit, num >> (n-1), num & 1
"""

from math import log

def reverse(n):
    rev = 0
    while n > 0:
        rev = rev << 1
        if n & 1 == 1:
            rev ^= 1
        n = n >> 1
    return rev

def invert(n):
    bits = int(log(n, 2)) + 1
    ones = 2 ** bits - 1
    return n ^ ones

def print_bin(val):
    print(bin(val))


def main(n, k):
    num = 0b0
    size = 1
    i = 1
    while i < n:
        prev = num << (size + 1)
        print_bin(prev)
        middle = 1 << size
        print_bin(middle)
        if num > 0:
            last = invert(reverse(num)) << 1
            last = last + 1
        else:
            last = 1
        print_bin(last)
        num = prev + middle + last
        i += 1
        size = 2 * size + 1
        print(bin(num))
        print("%"*10)
    val = num >> (size - k)
    return val & 1

print(main(3, 1))
print(main(4, 11))
print(main(1, 1))
print(main(2, 3))
