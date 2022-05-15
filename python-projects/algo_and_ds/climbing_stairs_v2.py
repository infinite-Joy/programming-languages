"""
0
1 - 1
2 - 
3 - 1 + 1
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dp(n, memo=None):
            memo = {} if memo is None else memo
            if n in memo: return memo[n]
            
            if n == 0:
                return 0
            if n == 1:
                return 1
            else:
                memo[n] = dp(n-1, memo) + dp(n-2, memo)
                return memo[n]
            
            
            
        return dp(n+1)