"""
we can use two pointer here to find all the subarrays with the values
we can we can use the maxheap function with max 2 methods to find insert 2 sizes into it
time complexity: linear
space complexity: linear
from heapq import heappush, heappop
class Solution:
def minSumOfLengths(self, arr: List[int], target: int) -> int:
    heap = []
    leftpointer = 0
    rightpointer = 0
    curr_sum = arr[leftpointer]
    while rightpointer < len(arr):
        if curr_sum == target:
            rightpointer += 1
            size = rightpointer - leftpointer + 1
            heappush(heap, -size)
            if len(heap) > 2:
                heappop(heap)
        elif curr_sum < target:
            rightpointer += 1
            curr_sum += arr[rightpointer]
        else:
            curr_sum -= arr[leftpointer]
            leftpointer += 1
    if len(heap) < 2:
        return -1
    return sum(heap)




"""

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        if not arr: return -1
        heap = []
        leftpointer = 0
        rightpointer = 0
        curr_sum = arr[leftpointer]
        while rightpointer < len(arr):
            if curr_sum == target:
                size = rightpointer - leftpointer + 1
                rightpointer += 1
                leftpointer = rightpointer
                heappush(heap, -size)
                if len(heap) > 2:
                    heappop(heap)
                if rightpointer < len(arr):
                    curr_sum = arr[rightpointer]
            elif curr_sum < target:
                rightpointer += 1
                if rightpointer < len(arr):
                    curr_sum += arr[rightpointer]
            else:
                curr_sum -= arr[leftpointer]
                leftpointer += 1
        if len(heap) < 2:
            return -1
        return -sum(heap)



for two pointers check if you have negative numbers in the arr
otherwise it will wreak havoc
you can also try prefix sums to get to the understanding if there are multiple values
