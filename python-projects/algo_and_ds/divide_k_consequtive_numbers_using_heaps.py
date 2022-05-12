"""
sort the distinct chars arr first and put this in a queue
sort the numbers probably using a heap


"""

from heapq import heapify, heappop
from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        distinct_els = list(set(nums))
        heapify(distinct_els)
        counts = Counter(nums)
        
        while distinct_els:
            smallest = distinct_els[0]
            for i in range(k):
                counts[smallest+i] -= 1
                if counts[smallest+i] < 0:
                    return False
            # print(counts, distinct_els)
            while counts[distinct_els[0]] == 0:
                heappop(distinct_els)
                if len(distinct_els) == 0:
                    return True
                
        return True