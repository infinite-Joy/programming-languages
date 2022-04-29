"""
thinking of a dfs solution.

if possible will do a memoisation

"""


# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         def dfs(i, j, height):
#             j = min(j, len(height))
#             if i >= j:
#                 return 0
#             if i >= len(height):
#                 return 
#             curr_water = (j - i) * min(i, j)
#             curr_water = max(curr_water, dfs(i+1, j), dfs(i, j+1))
#             return curr_water
#         return dfs(0, 0, height)

def maxArea(height):

    def dfs(i, j, height):

        if i >= len(height) or j >= len(height):
            return 0
        if i > j:
            return 0

        curr_water = (j - i) * min(height[i], height[j])
        # print(i, j, curr_water)
        curr_water = max(curr_water,
            dfs(i+1, j, height), dfs(i, j+1, height))
        return curr_water

    return dfs(0, 0, height)


print(maxArea([1,8,6,2,5,4,8,3,7]))
# print(maxArea([1]))