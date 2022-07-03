"""
find which arr is the higher array
in the higher arr. find the contigous arr which has the biggest numbers that can be swapped.
return that number

basically a 2 pointer approach
"""


# class Solution:
#     def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
#         maxsum1 = sum(nums1)
#         maxsum2 = sum(nums2)
#         if maxsum1 < maxsum2:
#             nums1, nums2 = nums2, nums1
#             maxsum1, maxsum2 = maxsum2, maxsum1
#         i = 0
#         j = i
#         maxsum = 0
#         while i < len(nums1) and j < len(nums2):
#             thissum = maxsum1
#             while nums2[j] > nums1[j]:
#                 thissum -= nums1[j]
#                 thissum += nums2[j]
#                 j += 1
#             i = j + 1
#             j = i
#             maxsum = max(maxsum, thissum)
#         return maxsum


def base(nums1, nums2):
    maxsum1 = sum(nums1)
    maxsum2 = sum(nums2)
    i = 0
    j = i
    maxsum = 0
    while i < len(nums1) and j < len(nums2):
        thissum = maxsum1
        while j < len(nums2) and nums2[j] > nums1[j]:
            thissum -= nums1[j]
            thissum += nums2[j]
            j += 1
        print(i, j, maxsum, thissum)
        i = j + 1
        j = i
        maxsum = max(maxsum, thissum)
    return maxsum


def main(nums1, nums2):
    maxsum1 = sum(nums1)
    maxsum2 = sum(nums2)
    maxval = max(base(nums1, nums2), base(nums2, nums1))
    return maxval

nums1 = [20,40,20,70,30]
nums2 = [50,20,50,40,20]
print(main(nums1, nums2))