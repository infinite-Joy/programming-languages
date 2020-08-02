# Definition for singly-linked list.
# https://leetcode.com/problems/add-two-numbers/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    
    def addin(self, next1, next2, carry=0, prev_node=None):
        addition = next1 + next2 + carry
        base = addition % 10
        base_node = ListNode(base)
        if prev_node is not None:
            prev_node.next = base_node
        carry = addition // 10
        
        return base_node, carry
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        next1 = l1.next
        next2 = l2.next
        base_node, carry = self.addin(next1, next2)
        first_node = base_node
        while next1 and next2:
            base_node, carry = self.addin(next1, next2, carry, base_node)
            
            next1 = next1.next
            next2 = next2.next
            
        if next1 is not None:
            while next1:
                base_node, carry = self.addin(next1, 0, carry, base_node)
                next1 = next1.next
        elif next2 is not None:
            while next2:
                base_node, carry = self.addin(0, next2, carry, base_node)
                next2 = next2.next
        else:
            pass
        if carry > 0:
            self.addin(0, 0, carry, base_node)
        return first_node
        