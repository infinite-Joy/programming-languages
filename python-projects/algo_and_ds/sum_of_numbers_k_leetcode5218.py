# """
# This looks like a bfs approach
# because here the point is to find the minimum possible size
# """

# from collections import deque

# class Solution:
#     def minimumNumbers(self, num: int, k: int) -> int:
#         candidates = []
#         c = k
#         while c <= num:
#             candidates.append(c)
#             c += 10
            
#         def get_next_vals(num, k):
#             for c in candidates:
#                 if c <= num:
#                     yield num-c, c
#                 else:
#                     break
                    
#         def bfs(num, k):
#             queue = deque([(num, 0)]) # rem, curr, level
#             visited = {(num, 0): 0}
#             while queue:
#                 rem, curr = queue.popleft()
#                 level = visited[(rem, curr)]
#                 # business logic
#                 if rem == 0:
#                     return level
#                 for nextrem, nextval in get_next_vals(rem, k):
#                     if (nextrem, nextval) not in visited:
#                         queue.append((nextrem, nextval))
#                         visited[(nextrem, nextval)] = level+1
#             return -1
        
#         if num == 0:
#             return 0
        
#         return bfs(num, k)


# from collections import deque


# def main(num, k):
#     candidates = []
#     c = k
#     while c < num:
#         candidates.append(c)
#         c += 10
        
#     def get_next_vals(num, k):
#         for c in candidates:
#             if c <= num:
#                 yield num-c, c
#             else:
#                 break
                
#     def bfs(num, k):
#         queue = deque([(num, 0)]) # rem, curr, level
#         visited = {(num, 0): 0}
#         while queue:
#             print(queue)
#             print(visited)
#             rem, curr = queue.popleft()
#             level = visited[(rem, curr)]
#             # business logic
#             if rem == 0:
#                 return level
#             for nextrem, nextval in get_next_vals(rem, k):
#                 if (nextrem, nextval) not in visited:
#                     queue.append((nextrem, nextval))
#                     visited[(nextrem, nextval)] = level+1
#         return -1
    
#     return bfs(num, k)


# num = 58
# k = 9
# print(main(num, k))


import math


def main(num, k):
    candidates = []
    if k == 0:
        c = 10
    else:
        c = k
    while c <= num:
        candidates.append(c)
        c += 10
        
    def dp(num, memo=None):
        memo = {} if memo is None else memo
        if num in memo: return memo[num]

        if num < 0:
            return 0, False
        if num == 0:
            return 0, True
        minval = math.inf
        poss1 = False
        for c in candidates:
            if c <= num:
                res, poss = dp(num - c, memo)
                if poss:
                    poss1 = True
                    minval = min(minval, res)
        print(num, minval, poss1)
        memo[num] = (minval + 1, poss1)
        return minval + 1, poss1
    
    res, poss = dp(num)
    if poss: return res
    return -1


num = 58
k = 9
# print(main(num, k))

num = 4
k = 0
print(main(num, k))