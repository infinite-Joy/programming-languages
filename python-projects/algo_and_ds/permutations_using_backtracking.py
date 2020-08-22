# again looks like a backtracking solution
# complexity is nPr

def backtrack(sofar, rest):
    if rest == []:
        yield tuple(list(sofar))
    else:
        for i, num in enumerate(list(rest)):
            # make move
            nextnum = sofar + [num]
            remaining = rest[:i] + rest[i+1:]

            # backtracking
            yield from backtrack(nextnum, remaining)

            # no need to do any unmake move as the operations are separate

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        for val in backtrack([], nums):
            sol.append(val)
        return sol

arr = [1,2,3]
s = Solution()
print(s.permute(arr))
