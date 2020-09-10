class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twosum = {}
        for i, item in enumerate(nums):
            if item in twosum:
                return [twosum[item], i]
            twosum[target - item] = i
        return [-1, -1]
