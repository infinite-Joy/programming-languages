"""

merge k sorted lists together

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

basically to have a heap with the value and the id
heap is based the value

get the minimum value and replace that with the next item in the array

Merge all the linked-lists into one sorted linked-list and return it

1   3   5
2   3   5

"""

from heapq import heapify, heappop, heappush

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heap.append((lists[i].val, i, list[i]))
        heapify(heap)

        node = None
        head = None
        while heap:
            _, i, nnode = heappop(heap)
            if head is None:
                head = nnode
                node = head
            else:
                node.next = nnode
                node = nnode
            nnode = node.next
            if nnode:
                heappush(heap, (nnode.val, i, nnode))
        return head
