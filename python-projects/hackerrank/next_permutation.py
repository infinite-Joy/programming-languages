from typing import List
import itertools
def bruteforce(nums):
    """
    complexity: O(2n)
    """
    permutations = list(itertools.permutations(nums))
    permutations = list(set(permutations))
    permutations = sorted(permutations)
    print(permutations)
    for i, num in enumerate(permutations):
        if list(num) == nums:
            print(i)
            if i+1 == len(permutations):
                return list(permutations[0])
            return list(permutations[i+1])

def lineartime(nums, i):
    if i==0:
        nums.sort()
    if nums[i-1]>nums[i]:
        lineartime(nums, i-1)
    else:
        nums[i-1], nums[i] = nums[i], nums[i-1]


class Solution:
    def nextPermutation(self, nums: List[int], nums2) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = bruteforce(nums)
        for i in range(len(nums)):
            nums[i] = ans[i]
        print(nums)
        lineartime(nums2, len(nums)-1)
        print(nums2)

s = Solution()
#nums = [2,1,3]
#nums = [1,1,5]
#nums = [6,7,5,3,5,6,2,9,1,2,7,0,9]
#nums = [6,7,5,3,5]
nums1 = [1,3,2]
nums2 = [1,3,2]
print(nums1, nums2)
s.nextPermutation(nums1, nums2)
