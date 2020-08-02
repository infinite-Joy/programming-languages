"""
https://leetcode.com/problems/guess-number-higher-or-lower-ii/
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.
However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

answer
the interesting things about this problem is that for some a random pick, the amount is a binary tree
and even finding the maximum is a binary tree
hence we can do two levels of binary trees. since these are binary trees. hence the complexity is (logn)^2
"""

import math

def payment(n, pick, paid=0, minval=0, maxval=math.inf):
    if maxval > n:
        maxval=n
    mid = (maxval + minval)//2
    if mid == pick:
        return paid
    elif mid > pick:
        return payment(n, pick, paid+mid, minval, mid-1)
    else:
        return payment(n, pick, paid+mid, mid+1, maxval)

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        if n == 1:
            return 0
        return payment(n, n)
