from typing import List
# complexity is O(k * 2 ^ n')

def backtrack(nums: List[int], partialsol: List[int], target: int, currsum: int):
    print(nums, partialsol, target, currsum)
    if currsum == target:
        yield tuple(sorted(partialsol))
    else:
        for num in nums:
            if currsum + num <= target:
                # make move
                partialsol.append(num)

                yield from backtrack(nums, partialsol, target, currsum+num)

                # unmake move
                partialsol.pop()


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = set()
        for values in backtrack(candidates, [], target, 0):
            sol.add(values)
        return [list(x) for x in sol]

s = Solution()
candidates = [2,3,6,7]
target = 7
print(s.combinationSum(candidates, target))
