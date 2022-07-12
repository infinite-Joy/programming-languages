# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""

this should be easy
loop for n values and then put head as the one to remove

"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)
    def __str__(self):
        return str(self.val)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prevnode = None
        pointer = head # 1
        nnode = head # 1
        for _ in range(n):
            pointer = pointer.next # none
        while pointer: # this will not happen
            pointer = pointer.next
            prevnode = nnode
            nnode = nnode.next
        # remove the node
        if prevnode: 
            prevnode.next = nnode.next
            return head
        return prevnode

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    prevnode = None
    pointer = head # 1
    nnode = head # 1
    for _ in range(n):
        pointer = pointer.next # none
    print(pointer)
    while pointer: # this will not happen
        pointer = pointer.next
        prevnode = nnode
        nnode = nnode.next
    # remove the node
    if prevnode: 
        prevnode.next = nnode.next
        return head
    if nnode:
        return nnode.next

arr = [1,2]
n = 2
head = ListNode(arr[0])
node = head
for el in arr[1:]:
    newnode = ListNode(el)
    node.next = newnode
    node = newnode
res = removeNthFromEnd(head, n)
print('output')
while res:
    print(res.val, '>', end=' ')
    res = res.next