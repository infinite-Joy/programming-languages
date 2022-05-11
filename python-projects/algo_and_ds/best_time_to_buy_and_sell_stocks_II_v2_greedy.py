"""
greedy solution. buy when the prices are the lowest and sell when the prices are the highest

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.append(0)
        start = 0
        maxprice = prices[0]
        minprice = prices[0]
        res = 0
        for i in range(1, len(prices)):
            maxprice = max(maxprice, prices[i])
            if prices[i] < maxprice:
                res += maxprice - minprice
                minprice = maxprice
                maxprice = 0
            minprice = min(minprice, prices[i])
        return res


# easier solution is to just buy and sell everyday. and hold if the prices are coming down.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        
        profit = 0
        j = 1
        while j < len(prices):
            if prices[j] > prices[j-1]:
                profit += prices[j] - prices[j-1]
            j += 1
        return profit