"""
for coin change all the values need to be handled.

space : O(amount)
time: O(len(coins)*amount)


"""


import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dp(coins, amount, memo=None):
            memo = {} if memo is None else memo
            if amount in memo: return memo[amount]
            
            if amount < 0:
                return math.inf
            if amount == 0:
                return 0
            else:
                min_val = math.inf
                for c in coins:
                    cval = dp(coins, amount - c, memo) + 1
                    min_val = min(min_val, cval)
                memo[amount] = min_val
                return min_val
                
        def main(coins, amount):
            coins.sort()
            out = dp(coins, amount)
            if out == math.inf:
                return -1
            else:
                return out
                
        return main(coins, amount)