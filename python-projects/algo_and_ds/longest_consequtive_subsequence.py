"""
this will be done in linear time.

"""


from functools import lru_cache

g = {}
        
def buildgraph(arr):
    elems = {e: i for i, e in enumerate(arr)}
    graph = {}
    for i in range(len(arr)):
        if arr[i] + 1 in elems:
            graph[i] = elems[arr[i] + 1]
    return graph
    
# @lru_cache()
def dfs(i, g):
    if i == -1:
        return 0
    else:
        return 1 + dfs(g.get(i, -1), g)
    
def main(arr):
    g = buildgraph(arr)
    maxval = 0
    for i in range(len(arr)):
        maxval = max(maxval, dfs(i, g) + 1)
    return maxval

arr = [2,6,1,9,4,5,3]
print(main(arr))