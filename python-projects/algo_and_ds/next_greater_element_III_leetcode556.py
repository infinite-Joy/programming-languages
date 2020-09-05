# https://leetcode.com/problems/next-greater-element-iii/

"""

next greater element
556. Next Greater Element III
smallest next greater element

bruteforce is to start from the element and then keep on incrementing till all the  digits match.

this is O(digits * digits)

example 1 2 3 4 5
out     2 1 3 4 5

this becomes an O(n)

another example 5463
out  5634

    5   6   3   4
            _

    6   7   2   0   1
                _

    2   5   3   5   3
            _
    2   5   5   3   3

    2   3   0   2   4   1
                        _

looks like a simple algo
    start from the last
    check curr with curr + 1, if greater than swap. and return

time complexity: O(digits)
space complexity: O(digits)

"""


from math import inf
from itertools import accumulate
class Solution:

    def next_greater(self, nums):
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                return i
    def next_val(self, nums, partition):
        next_val = inf
        position = partition + 1
        val = nums[partition]
        for i in range(partition+1, len(nums)):
            if nums[i] > val:
                next_val = min(nums[position], nums[i])
                if next_val == nums[i]:
                    position = i
        return position
    def count_sort(self, nums, start):
        print(nums[start:])
        maxval = -inf
        for i in range(start, len(nums)):
            maxval = max(maxval, int(nums[i]))

        placeholder = [0 for _ in range(maxval+1)]
        for elem in range(start, len(nums)):
            placeholder[int(nums[elem])] += 1
        print('placeholder', placeholder)

        placeholder = list(accumulate(placeholder))
        print(placeholder)

        vals = [None for _ in nums]
        for i in range(len(nums) - 1, start - 1, -1):
            item = int(nums[i])
            placeholder[item] -= 1
            vals[placeholder[item]] = nums[i]
            print(vals)
        print(vals)
        
        for i in range(start, len(nums)):
            nums[i] = vals[i - 1]

    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        print(nums)

        # find the partition
        partition = self.next_greater(nums)
        if partition is None:
            return -1
        print(partition)

        # find the next val position to do the swapping
        next_val_pos = self.next_val(nums, partition)
        print(next_val_pos)

        # now do the swapping
        nums[partition], nums[next_val_pos] = nums[next_val_pos], nums[partition]

        # sort the remaining
        self.count_sort(nums, partition + 1)
        print(nums)
        #right_portion = sorted(nums[partition + 1:])
        ##print(right_portion)
        #nums = nums[:partition + 1] + right_portion
        nums = int("".join(nums))
        if nums > n:
            if nums >= 2**31:
                return nums
        return -1

#not working

sol = Solution()
print(sol.nextGreaterElement(230241))
assert sol.nextGreaterElement(230241) == 230412
#
#print(sol.nextGreaterElement(12443322))
#assert sol.nextGreaterElement(12443322) == 13222344

# nums = 1200000
# print(sol.nextGreaterElement(nums))
# assert sol.nextGreaterElement(nums) == 2000001


# finally the solution using swapping partition and radix sort
