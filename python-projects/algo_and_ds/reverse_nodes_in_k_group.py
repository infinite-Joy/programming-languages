# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

while not finish
get head and last and next head of the linked list
reverse the linked list
head -> next head
head = last

"""
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        def reverse(head, last):
            this = head
            prev = None
            nextnode = this.next
            while this != last:
                this.next = prev
                prev = this
                this = nextnode
                nextnode = nextnode.next
            return last, head

        def find_pointers(head, k):
            orig_head = head
            node = head
            for i in range(k):
                node = head.next
                if node is None:
                    return orig_head, head, None
                head = node
                
            head, last = reverse(orig_head, node)
            return head, last, node.next
        
        def main(head, k):
            firsthead = None
            nexthead = head
            while nexthead:
                head, last, nexthead = find_pointers(head, k)
                if firsthead is None:
                    firsthead = head
            return firsthead
        
        return main(head, k)