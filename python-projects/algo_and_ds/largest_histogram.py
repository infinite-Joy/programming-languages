"""
divide and conquer algorithm


the complexity is O(nlogn)




"""

import math

def largestRectangleArea(heights) -> int:
    def histogram_area(A, left, right):
        print(left, right)
        if left > right:
            return 0
        
        minidx = left
        minimum = math.inf
        for i in range(left, right+1):
            if min(A[i], minimum) == A[i]:
                minimum = A[i]
                minidx = i
        maxarea = minimum * (right - left + 1)
        leftarea = histogram_area(A, left, minidx-1)
        rightarea = histogram_area(A, minidx+1, right)
        
        return max(maxarea, leftarea, rightarea)
    
    return histogram_area(heights, 0, len(heights)-1)
    # return histogram_area(heights, 0, 3)


heights = [2,1,5,6,2,3]
print(heights)
print(largestRectangleArea(heights))