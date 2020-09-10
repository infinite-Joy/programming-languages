"""

x of a kind in a deck of cards

leetcode 914

[1,2,3,4,4,3,2,1]
1   2   3   4   4   3   2   1
deck = [1,1,1,2,2,2,3,3]
1   0   1   12  1   12  123     12

this is not woring

will have to get the counts and then will have to check if the values are coprime

using gcd

"""

from collections import Counter
from typing import List
class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
    def gcd_arr(self, arr, i, j):
        if j == len(arr) - 1:
            return self.gcd(arr[i], arr[j])
        return self.gcd(arr[i], self.gcd_arr(arr, j, j + 1))
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        __import__('pdb').set_trace()
        deck_counts = Counter(deck)
        minval = min(deck_counts.values())
        distinct_vals = list(set(deck_counts.values()))
        if len(distinct_vals) == 1 and distinct_vals[0] >= 2:
            return True
        if len(distinct_vals) >= 2 and self.gcd_arr(distinct_vals, 0, 1) >= 2:
            return True
        return False

deck = [1,1,1,2,2,2,3,3]
sol = Solution()
print(sol.hasGroupsSizeX(deck))
