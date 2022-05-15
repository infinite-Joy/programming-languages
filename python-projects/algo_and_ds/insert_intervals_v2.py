"""
this can be done using binary search

search the second number in the first values.
then if first number less than second number of prev interval merge. else put this in the array.

"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        def binsearch(intervals, newInterval):
            start = 0
            end = len(intervals)
            first, sec = newInterval

            while start < end:
                mid = int((start + end) / 2)
                if sec < intervals[mid][0]:
                    end = mid
                else:
                    start = mid + 1
            return start
        
        def main(intervals, newInterval):
            first, sec = newInterval
            insertion_point = binsearch(intervals, newInterval)
            left = intervals[:insertion_point]
            right = intervals[insertion_point:]
            if len(left) == 0:
                return [newInterval] + intervals
            else:
                candidate = newInterval
                last = left.pop()
                while candidate[0] <= last[1] and len(left) > 0:
                    candidate = [last[0], candidate[1]]
                    last = left.pop()
                if candidate[0] <= last[1]:
                    candidate = [last[0], candidate[1]]
                return left + [candidate] + right
            
        return main(intervals, newInterval)


# not working for below code.

[[1,2],[3,5],[6,7],[8,10],[12,16]]
[4,8]

expected:
[[1,2],[3,10],[12,16]]
