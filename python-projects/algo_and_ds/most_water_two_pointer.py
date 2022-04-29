"""
thinking of a dfs solution.

if possible will do a memoisation

actually the dfs did not work. have a greedy solution based on two pointers.

"""

def maxArea(height):
    
    i = 0
    j = len(height) - 1
    max_water = 0
    
    while i < j:
        curr_water = (j - i) * min(height[i], height[j])
        max_water = max(max_water, curr_water)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
            
    return max_water



class Solution:
    def maxArea(self, height: List[int]) -> int:
        return maxArea(height)