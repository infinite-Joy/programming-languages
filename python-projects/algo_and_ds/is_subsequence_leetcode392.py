"""

is subsequence

https://leetcode.com/problems/is-subsequence/ leetcode 392

this can be done using the 2 pointer method

time: O(n+m)
space: O(1)

"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # s = "abc", t = "ahbgdc"
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s) - 1

"""
now if there are a lot of queries on the target then we will need to preprocess the target into some DS

what we will do is same the indices in a hashmap

and then do binary search on the problem to see if the value is present or not

if we are reaching the end that means we are not going to find the value and hence return False

t = "aaaabb"
a,b

hashmap = {a:[0, 1, 2, 3], b: [4, 5]}
found = 0
bs(0, hashmap[a]) there so return found = 1
bs[1, hashmap[b]] return 0
bs[2, hashmap[b]] return 0 found++
bs[3, hashmap[b]] return 0 found++
bs[4, hashmap[b]] there

if it were abd, then hashmap[d] is not there hence false
if abbb

time complexity for each query: O(mlogn) where m is the size of the query and n is the size of the target
space complexity: O(n)

"""

from bisect import bisect_left
from collections import defaultdict
from typing import List

class Solution:
    def preprocess(self, t):
        hashmap = defaultdict(list)
        for i, item in enumerate(t):
            hashmap[item].append(i)
        return hashmap
    def isSubsequence(self, s: str, t: str) -> bool:
        print(s, t)
        hashmap = self.preprocess(t)
        print(hashmap)

        found = 0
        for ch in s:
            if ch in hashmap:
                idx = bisect_left(hashmap[ch], found)
                print(idx)
                if idx == len(hashmap[ch]):
                    return False
                found = hashmap[ch][idx] + 1
            else:
                return False
        return True

s = "abc"
t = "ahbgdc"
sol = Solution()
print(sol.isSubsequence(s, t))

s = "ab"
t = "bab"
sol = Solution()
print(sol.isSubsequence(s, t))

s = "axc"
t = "ahbgdc"
sol = Solution()
print(sol.isSubsequence(s, t))

s = "aaaaaa"
t = "bbaaaa"
sol = Solution()
print(sol.isSubsequence(s, t))
