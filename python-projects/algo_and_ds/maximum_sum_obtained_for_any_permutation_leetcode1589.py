"""
maximum sum obtained on any permutations

    requests 1, 3 and 0, 1

    1   2   3   4   5


    have to calculate for that particular permutation

    i can probably try the greeddy approach.
    else will have to do using the backtracking

    this looks like a sorting problem.
    sort them and then put the maximum numbers in the sorted position

    basically a merge interval solution. once the intervals are merged then find the total elements in the intervals and then find the sum

    1, 3 and 0, 1 becomes 0, 3
    you have to see which intervals are counted number of times. basically sort the intervals thats it. no need to merge

    0   1
        1   2   3
    4   10   3   2

    maybe i can take a hashmap of the intervals and then take the heap and then find the intervals in that way

    usign heaps and sorting

"""

from heapq import heapify, heappush, heappop
from collections import Counter, defaultdict
class Solution:
    def counter(self, nums):
        counts = defaultdict(int)
        for ranges in nums:
            for item in ranges:
                counts[item] += 1
        return counts
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        if not nums: return 0
        nums = [-x for x in nums]
        heapify(nums)
        intervals = self.counter(list(range(r[0], r[1]+1)) for r in requests)
        intervals = sorted(list(intervals.items()), key=lambda x: x[1], reverse=True)
        # print(intervals)
        total = 0
        for val, count in intervals:
            curr_high = heappop(nums)
            # print(val, count, curr_high)
            total += -curr_high * count
        return total
