"""
this is possibly a dp problem

an easier way probably is greedy.



"""


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        rem = [c-r for (c, r) in zip(capacity, rocks)]
        rem.sort()
        c = 0
        for r in rem:
            additionalRocks = additionalRocks - r
            if additionalRocks < 0:
                return c
            else:
                c += 1
        return c
            
        
#         def dp(capacity, rocks, i, additional_rocks):
#             if i < 0:
#                 return 0
#             if additional_rocks < 0:
#                 return 0
#             else:
#                 donotuse = dp(capacity, rocks, i-1, additional_rocks)
#                 useit = dp(capacity, rocks, i-1, additional_rocks-(capacity[i]-rocks[i]))
#                 return max(useit+1, donotuse)
            
#         return dp(capacity, rocks, len(capacity)-1, additionalRocks)