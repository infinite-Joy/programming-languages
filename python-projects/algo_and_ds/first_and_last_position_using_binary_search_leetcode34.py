from typing import List

def find_left(nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            import time; time.sleep(0.5)
            print(low, high)
            if low == high or low + 1 == high:
                if nums[low] == target:
                    return low
                if nums[high] == target:
                    return high
                else:
                    return -1
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid
            else:
                high = mid
def find_right(nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            import time; time.sleep(0.5)
            print(low, high)
            if low == high or low + 1 == high:
                if nums[high] == target:
                    return high
                if nums[low] == target:
                    return low
                else:
                    return -1
            mid = (low + high) // 2
            if nums[mid] <= target:
                low = mid
            else:
                high = mid
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # we can probably do this in 2 passes
        # first we find the left one then we do the right one
        # left one
        # time complexity : O(logn)
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return -1

        left = find_left(nums, target)
        right = find_right(nums, target)

        return [left, right]

s = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(s.searchRange(nums, target))

nums = [5,7,7,8,8,10]
target = 6
print(s.searchRange(nums, target))

nums = [2, 2]
target = 2
print(s.searchRange(nums, target))


