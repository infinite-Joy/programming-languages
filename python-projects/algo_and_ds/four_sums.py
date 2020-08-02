# https://leetcode.com/problems/4sum/
# solution is mapping using hashmaps

from itertools import combinations
from typing import List
from collections import defaultdict


class Solution:
    def _fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        print(nums)
        mapping = defaultdict(list)
        solution = {}
        for combination in combinations(nums, 3):
            mapping[target-sum(combination)].append(combination)
        print(mapping)
        for item in nums:
            if item in mapping:
                for comb in mapping[item]:
                    answer = sorted([item] + list(comb))
                    if tuple(answer) not in solution:
                        solution[tuple(answer)] = True
                        yield answer

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        vals = []
        for sol in self._fourSum(nums, target):
            vals.append(sol)
        return vals


nums = [1, 0, -1, 0, -2, 2]
target = 0

for s in Solution().fourSum(nums, target):
    print(s)
