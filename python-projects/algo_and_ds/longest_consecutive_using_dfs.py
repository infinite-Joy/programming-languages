def dfs(val):
    if val not in elems:
        return 0
    else:
        return 

def find(x, parents):
    while parents[x] != x:
        x = parents[x]
    return x

def union(x, y)


def main(nums):
    distinctelems = set(nums)
    g = {x: x+1 for x in nums if x+1 in distinctelems}
    parents = {}
    for el in nums:
        if el - 1 in g:
            parents[el] = el - 1
        else:
            parents[el] = el











    distinctelems = set(nums)
    visited = {}
    max_cons = 0
    print(f'{distinctelems=}')
    for elem in nums:
        if elem not in visited:
            max_cons = max(
                max_cons, dfs(elem, distinctelems, visited)
            )
    return max_cons

nums = [3, 4, 2]
print(main(nums))