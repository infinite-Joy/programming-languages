"""

median finder in a stream of numbers

https://leetcode.com/problems/find-median-from-data-stream/

this is done using the min heap for the greater elements
and max heap for the smaller elements

space complexity: O(n)
time complexity: logn for the insert and O(1) for the findmedian


"""

from heapq import heappush, heappop
from math import fabs

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.bigger_elements = []
        self.smaller_elements = []
        self.median = None

    def resize(self):
        if len(self.bigger_elements) - len(self.smaller_elements) > 1:
            elem = heappop(self.bigger_elements)
            heappush(self.smaller_elements, -elem)
            return
        if len(self.smaller_elements) - len(self.bigger_elements) > 1:
            elem = heappop(self.smaller_elements)
            heappush(self.bigger_elements, -elem)
            return

    def addNum(self, num: int) -> None:
        if self.median is None:
            self.median = num
            heappush(self.smaller_elements, -num)
            return

        # find where the element should be placed and then push the element to
        # the respective heap
        if num > self.median:
            heappush(self.bigger_elements, num)
        else:
            heappush(self.smaller_elements, -num)

        # if the unbalancing is more than 2 then resize the arr
        self.resize()

        # get the median
        if len(self.smaller_elements) == len(self.bigger_elements):
            small = -self.smaller_elements[0]
            big = self.bigger_elements[0]
            self.median = (small + big) / 2
            return
        if len(self.smaller_elements) == len(self.bigger_elements) + 1:
            self.median = -self.smaller_elements[0]
            return
        if len(self.bigger_elements) == len(self.smaller_elements) + 1:
            self.median = self.bigger_elements[0]
            return

    def findMedian(self) -> float:
        return float(self.median)



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
