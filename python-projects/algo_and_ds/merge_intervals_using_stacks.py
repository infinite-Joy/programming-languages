"""
merge intervals

bringing in an n2 solution which is the brute force
    so you check each and every and then merge them if fall within the same range

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

[[1,3],[2,6],[8,10],[15,18]]
    _

1:6, 8:10 15:18

time complexity: O(nlogn)
space complexity: O(n)

"""

def merge_intervals(intervals):
    if len(intervals) <= 1:
        return intervals
    intervals.sort()
    groups = [] # working with the stack

    for i in range(len(intervals)):
        if len(groups) == 0:
            groups.append(intervals[i])
        else:
            prev = groups.pop()
            if prev[1] >=intervals[i][0]:
                prev[1] = max(prev[1], intervals[i][1])
                groups.append(prev)
            else:
                groups.append(prev)
                groups.append(intervals[i])

    return groups
