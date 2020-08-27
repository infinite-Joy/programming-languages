"""
https://leetcode.com/problems/top-k-frequent-words/

i am thinking of this using heap

so basically for the count mapp
then convert the count map to an arr of values and counts
and then make a heap out of them. that can be done in O(n)
and then do the k greatest.

so the time complexity is O(n)
and space complexity O(n)

"""
from typing import List
from collections import defaultdict
from heapq import heapify, heappush, heappop
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = defaultdict(int)
        for word in words:
            counts[word] += 1

        counts = [(-count, word) for word, count in counts.items()]
        heapify(counts)

        sol = []
        elems = 0
        while elems < k and counts:
            sol.append(heappop(counts)[1])
            elems += 1
        return sol


# test cases
arr = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
s = Solution()
print(s.topKFrequent(arr, k))
