"""

Input: sweetness = [1,2,3,4,5,6,7,8,9], K = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]


we will need to do binary search on the sweetness parameter
such that the resultant sweetness is maximised
and for each sweetness we will need to see if we can make k + 1 chunks

algorithm:

check ability sweetness val k:
    sum = 0
    chunks = 0
    for item in sweetness:
        sum += item
        if sum > val:
            chunks += 1
            sum = 0
    if chunks > k:
        return True


binary search:
    starting low = 1
    starting high = sum(sweetness)

    while low < high:
        find mid of low and high
        if able to cut to k + 1 pieces:
            update low to mid + 1
        else:
            update high to midthe

time complexity: O(size of the arr * log(sum of the arr))


"""


from typing import List
class Solution:
    def valid_min_sweetness(self, sweetness, val, k):
        running_sum = 0
        chunks = 0
        for item in sweetness:
            running_sum += item
            if running_sum > val:
                chunks += 1
                running_sum = 0
        if chunks > k:
            return True

    def binary_search(self, sweetness, k):
        low = 1
        high = sum(sweetness)

        while low < high:
            mid = (low + high) / 2
            if self.valid_min_sweetness(sweetness, mid, k):
                low = mid + 1
            else:
                high = mid
        return int(low)

    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        return self.binary_search(sweetness, K)

# test cases
sweetness = [1,2,3,4,5,6,7,8,9]
K = 5
sol = Solution()
print(sol.maximizeSweetness(sweetness, K))

sweetness = [5,6,7,8,9,1,2,3,4]
K = 8
sol = Solution()
print(sol.maximizeSweetness(sweetness, K))

sweetness = [1,2,2,1,2,2,1,2,2]
K = 2
sol = Solution()
print(sol.maximizeSweetness(sweetness, K))
