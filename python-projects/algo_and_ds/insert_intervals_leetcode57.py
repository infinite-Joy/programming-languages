"""

insert intervals

since this is sorted, we can od it in O(size of the arr)



"""

from typing import List
class Solution:
    def join(self, int1, int2):
        if int2 < int1:
            int1, int2 = int2, int1
        if int1[1] >= int2[0]:
            return None, [min(int1[0], int2[0]), max(int1[1], int2[1])]
        else:
            return int1, int2

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals and newInterval:
            return [newInterval]
        if not newInterval and intervals:
            return intervals
        sol = []
        for item in intervals:
            int1, newInterval = self.join(item, newInterval)
            if int1:
                sol.append(int1)
        sol.append(newInterval)
        return sol

# test casd
intervals = [[1,3],[6,9]]
newInterval = [2,5]
sol = Solution()
print(sol.insert(intervals, newInterval))

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
sol = Solution()
print(sol.insert(intervals, newInterval))

#  you can implement Binary search here as well but this will not reduce the
#  time complexity.
