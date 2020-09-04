"""

122. Best Time to Buy and Sell Stock II

here also looks like we can be greedy

although bringing up a greedy soltion is alwaus risky, it may not be right

# although i came up with the solution on my own and looked like a greedy solution will work
# why this works can be seen here
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/39404/Shortest-and-fastest-solution-with-explanation.-You-can-never-beat-this.

"""

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

