"""

https://leetcode.com/problems/meeting-rooms-ii/

meeting rooms

Input: [[0, 30],[5, 10],[6, 11],[15, 20]]
Output: 2

so we will need to sort the arr

and then use the 2 pointer method

time complexity: O(n)
space complexity: O(1)

this is similar to the merge intervals code

"""

from typing import List
from heapq import heappush, heapreplace

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1: return len(intervals)

        intervals.sort()

        heap = []
        for interval in intervals:
            start, end = interval
            if heap and heap[0] <= start:
                # meaning 2 people can use the same room
                heapreplace(heap, end)
            else:
                heappush(heap, end)

        return len(heap)

intervals = [[0, 30],[5, 10],[15, 20]]
s = Solution()
#print(s.minMeetingRooms(intervals))

intervals = [[9,10],[4,9],[4,17]]
s = Solution()
print(s.minMeetingRooms(intervals))
