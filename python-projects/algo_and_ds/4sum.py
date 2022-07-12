"""
basically this is the two sum made into n-sum
"""

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = []
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                low = j + 1
                high = len(nums) - 1
                while low < high:
                    thistarget = nums[i] + nums[j] + nums[low] + nums[high]
                    if thistarget == target:
                        quadruplets.append([nums[i] , nums[j] , nums[low] , nums[high]])
                    elif thistarget < target:
                        low += 1
                    else:
                        high -= 1
        return quadruplets


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    quadruplets = []
    nums.sort()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            low = j + 1
            high = len(nums) - 1
            while low < high:
                thistarget = nums[i] + nums[j] + nums[low] + nums[high]
                if thistarget == target:
                    values = [nums[i] , nums[j] , nums[low] , nums[high]]
                    if values not in quadruplets:
                        quadruplets.append([nums[i] , nums[j] , nums[low] , nums[high]])
                    low += 1
                    high -= 1
                elif thistarget < target:
                    low += 1
                else:
                    high -= 1
    return quadruplets

nums = [2,2,2,2,2]
target = 8
print(fourSum(nums, target))