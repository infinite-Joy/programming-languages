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

"""

from typing import List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Solution:
    def create_linked_list(self, pushed, return_elem):
        prevnode = None
        return_node = None
        for val in pushed:
            node = Node(val)
            if prevnode:
                prevnode.next = node
            node.prev = prevnode
            if val == return_elem:
                return_node = node
            prevnode = node
        node.next = None
        return return_node
    def restructure(self, node):
        prevnode = None
        nextnode = None
        if node.prev:
            prevnode = node.prev
        nextnode = node.next
        if prevnode:
            prevnode.next = nextnode
        if nextnode:
            nextnode.prev = prevnode
        node.next = None
        node.prev = None
        if prevnode:
            return prevnode
        return nextnode
    def check(self, node, popped):
        for val in popped:
            print(val, node.val)
            if node.val == val:
                node = self.restructure(node)
            elif node.next and node.next.val == val:
                self.restructure(node.next)
            else:
                return False
        return node is None
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if pushed and popped:
            # the main logic
            node = self.create_linked_list(pushed, popped[0])
            return self.check(node, popped)
        else:
            return True


# test cases
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
sol = Solution()
#print(sol.validateStackSequences(pushed, popped))

pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
sol = Solution()
#print(sol.validateStackSequences(pushed, popped))

pushed = [1,0]
popped = [1,0]
sol = Solution()
print(sol.validateStackSequences(pushed, popped))
