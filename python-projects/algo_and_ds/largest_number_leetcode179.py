"""

leetcode 179

Given a list of non negative integers, arrange them such that they form the largest number.

Input: [3,30,34,5,9]
Output: "9534330"

so basically need to implement radix sort in the opposite order

radix sort complexity : O(size * digits)
space complexity is constant as that is just between 0 - 9

basically lexicographic sorting

"""

from math import log10
from itertools import accumulate
from typing import List
class Solution:
    def count_sort(self, str_nums, place_val):
        placeholder = [0 for _ in range(10)]
        for i in range(len(str_nums)):
            placeholder[int(str_nums[place_val])] += 1
        placeholder = list(accumulate(placeholder))
        output = [None for _ in str_nums]
        for number in str_nums:
            pos = int(number[place_val])
            placeholder[pos] -= 1
            output[placeholder[pos]] = number
        return output


    def radix_sort(self, str_nums, digits_arr):
        placeholder = [0 for _ in range(10)]
        for p in range(digits):
            str_nums = self.count_sort(str_nums, digits_arr, p)

        # rectify the digits
        for num, digits in len(str_nums):
            pass # TODO to be implemented
        return str_nums

    def largestNumber(self, nums: List[int]) -> str:
        # convert all to strings
        digits_arr = [(int(log10(n)) + 1) for n in nums]
        maxdigits = max(digits_arr)
        str_nums = []
        for i, item in enumerate(nums):
            digits = digits_arr[i]
            rem = maxdigits - digits
            after_padding = item * (10 ** rem)
            str_nums.append(str(after_padding))

        # now do the sorting
        str_nums = self.radix_sort(str_nums, digits)

# using radix sort is too complicated

###########################

from math import log10
from itertools import accumulate
from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        print(nums)
        # convert all to strings
        digits_arr = [(int(log10(n)) + 1) for n in nums]
        maxdigits = max(digits_arr)
        str_nums = []
        for i, item in enumerate(nums):
            digits = digits_arr[i]
            rem = maxdigits - digits
            after_padding = item * (10 ** rem)
            str_nums.append((str(after_padding), digits))

        print(str_nums)
        # now do the sorting
        # of course this would do the sorting for the first element
        # if 2 elements are the same then the second element which has the less
        # number of digits would get the preference which is fine
        str_nums.sort(key=lambda x: x[0], reverse=True)
        print(str_nums)


        # now rectify
        out = []
        for num, digit in str_nums:
            out.append(num[:digit])

        # now join them to get the output
        return "".join(out)

arr = [3,30,34,5,9]
sol = Solution()
print(sol.largestNumber(arr))
