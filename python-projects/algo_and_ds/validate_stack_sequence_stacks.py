"""

validate stack sequence

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1


Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

        1   2

so basically a linkedlist would make most sense here

now using the stack Solution

"""

from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        poppedindex = 0
        for pushedval in pushed:
            stack.append(pushedval)
            print(pushedval, stack)
            while stack and stack[-1] == popped[poppedindex]:
                stack.pop()
                poppedindex += 1
        print(stack, poppedindex)
        if poppedindex == len(popped):
            return True
        return False


# test cases
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
sol = Solution()
print(sol.validateStackSequences(pushed, popped))

pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
sol = Solution()
print(sol.validateStackSequences(pushed, popped))

pushed = [1,0]
popped = [1,0]
sol = Solution()
print(sol.validateStackSequences(pushed, popped))
