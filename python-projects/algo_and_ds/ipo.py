"""

for each we can add the 

greedy solution
we sort based on the capital that is provided and the one that we have currently
based on that we choose the one with the highet profits
and for the answer we add the profits of the chosen projects.


"""

from heapq import heappush, heappop


def find_max_capital(profits, capital, k, w):
    cp = sorted(list(zip(capital, profits)))
    profit_heap = []
    curr = w
    j = 0
    for i in range(k):
        while j < len(cp) and curr >= cp[j][0]:
            heappush(profit_heap, (-cp[j][1], j))
            # curr_max_capital = cp[profit_heap[0][1]][1]
            j += 1
        if profit_heap:
            max_capital = heappop(profit_heap)[1] # once we have accepted a project we should probably not use that anymore.
            curr_max_capital = cp[max_capital][1]
            curr += curr_max_capital
    return curr


# k = 2
# w = 0
# profits = [1,2,3]
# capital = [0,1,1]
# print(find_max_capital(profits, capital, k, w))


# k = 3
# w = 0
# profits = [1,2,3]
# capital = [0,1,2]
# print(find_max_capital(profits, capital, k, w))

k = 1
w = 0
profits = [1,2,3]
capital = [1,1,2]
print(find_max_capital(profits, capital, k, w))

# ===================

# current implementation

from heapq import heappop, heappush

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        def find_max_capital(profits, capital, k, w):
            cp = sorted(list(zip(capital, profits)))
            profit_heap = []
            curr = w
            j = 0
            for i in range(k):
                while j < len(cp) and curr >= cp[j][0]:
                    heappush(profit_heap, (-cp[j][1], j))
                    # curr_max_capital = cp[profit_heap[0][1]][1]
                    j += 1
                # once we have accepted a project we should probably not use that anymore.
                if profit_heap:
                    max_capital = heappop(profit_heap)[1] 
                    curr_max_capital = cp[max_capital][1]
                    curr += curr_max_capital
            return curr
        
        return find_max_capital(profits, capital, k, w)