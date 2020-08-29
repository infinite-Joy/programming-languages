"""

https://www.careercup.com/question?id=5412018236424192

Given a linked list where apart from the next pointer,
 every node also has a pointer named random which can
 point to any other node in the linked list. Make a copy of the linked list.

 1 - 2 - 3 - 4

 random 1 - 3, 2 - 4

 algo
    1    2   3   4
    |  / | / | / |
    1    2   3   4

    change the pointers to similar to above

    b = a.random
    a.next.random = a.random.next

    now change the next pointers
    head = head.next
    a.next.next = a.next.next.next
    node = node.next

time complexity: O(n)
space complexity: O(1)

"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # make the copy
        node = head
        while node:
            copynode = Node(node.val)
            nnode = node.next
            node.next = copynode
            copynode.next = nnode
            node = nnode

        # specify the random nodes
        node = head
        while node:
            random_node = node.random
            if random_node:
                node.next.random = random_node.next
            else:
                node.next.random = None
            node = node.next.next

        # rectify the next nodes to point to the actual nodes
        if head:
            head1 = head.next
            node = head
            while node:
                node1 = node.next
                nnode = node1.next
                if nnode:
                    node1.next = nnode.next
                    node = nnode
                else:
                    node1.next = None
                    node = None
            return head1
