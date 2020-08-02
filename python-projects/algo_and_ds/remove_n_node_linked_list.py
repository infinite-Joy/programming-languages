"""
Given a linked list, remove the n-th node from the end of list and return its head.
Example:
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
we can have something called the previous, target and the next and  now.
and we will have the count variable
==============================================================
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return "Node: {}".format(self.val)
def delete_nth_node(head, n):
    count = 0
    previous = None
    target = None
    next = None
    now = head
    while now is not None:
        import time; time.sleep(1)
        print("count, previous, target, next, now")
        print(count, previous, target, next, now)
        count += 1
        if count - n == 1:
            previous = head
            target = previous.next
            next = target.next
        elif count - n + 1 == 1:
            target = head
            next = target.next
        elif count - n + 2 == 1:
            next = head
        else:
            if previous is not None: previous = previous.next
            if target is not None: target = target.next
            if next is not None: next = next.next
        now = now.next

    # i have reached the last
    if previous is None:
        head = target.next
    else:
        previous.next = next
    return head

def print_ll(head):
    if head is not None:
        print(head.val, end=" -> ")
        print_ll(head.next)


head = ListNode( 1, ListNode( 2, ListNode( 3, ListNode( 4, ListNode(5)))))
delete_nth_node(head, 2)
print_ll(head)

