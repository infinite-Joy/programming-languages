"""

palindrome linked list

https://leetcode.com/problems/palindrome-linked-list/

simple way is to store the numbers in an arr and then reverse  the array and then move through the arr again and see if they are the same

Could you do it in O(n) time and O(1) space?

1->2->2->1

what we can do is that will find the mid points and change the linked list pointers till the first mid

and then we will check the two linked list that we have and then compare them

a1  a2  a3  a4  a5  a6
_
mid1 mid2

a b c d mid1 mid2

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return "Node: {}".format(self.val)

def break_linkedlist(head):
    if head is None:
        return None, None
    mid1, mid2 = head, head
    change = False
    node = head
    while node:
        nnode = node.next
        print(node, mid1, mid2, change)
        change = not change # t, f, t
        if change:
            nmid2 = mid2.next # a2, a3
            mid2.next = mid1 # a1 -> a2, a2 -> a1
            mid1 = mid2 # a1, a2
            mid2 = nmid2 # a2, a3
        node = nnode # a2, a3, a4
    if mid1.next == mid1: # edge case
        mid1.next = None
        return change, mid1, mid1
    return change, mid1, mid2

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        odd, mid1, mid2 = break_linkedlist(head)
        #__import__('pdb').set_trace()
        print(odd, mid1, mid2)
        #__import__('pdb').set_trace()
        if odd and mid1 != mid2:
            node1 = mid1.next
            node2 = mid2
        else:
            node1 = mid1
            node2 = mid2

        while node1 and node2:
            if node1.val == node2.val:
                node1 = node1.next
                node2 = node2.next
            else:
                return False
        if node1 or node2:
            return False
        return True


# test code

#node = ListNode(1)
#sol = Solution()
##print(sol.isPalindrome(None))
#print(sol.isPalindrome(node))
#
#head = ListNode(1)
#n1 = ListNode(2)
#head.next = n1
#print(sol.isPalindrome(head))


"""

palindrome linked list

https://leetcode.com/problems/palindrome-linked-list/

simple way is to store the numbers in an arr and then reverse  the array and then move through the arr again and see if they are the same

Could you do it in O(n) time and O(1) space?

1->2->2->1

what we can do is that will find the mid points and change the linked list pointers till the first mid

and then we will check the two linked list that we have and then compare them

a1  a2  a3  a4  a5  a6
_
mid1 mid2

a b c d mid1 mid2

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)

# the above is a mess of a code. let me modify this in terms of fast and slow
# change the later half of the code
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #   1   2    3    4
        #       _       _
        fast, slow = head, head
        change = False
        count = 0
        while fast:
            count += 1
            print(fast, count)
            if count > 2:
                change = not change
            if change:
                slow = slow.next
            fast = fast.next
            if fast and slow:
                print('fast', fast, 'slow', slow, 'count', count)

        if count % 2 == 0:
            head2 = slow.next
        else:
            head2 = ListNode(slow.val)
            head2.next = slow.next
        node = head2
        __import__('pdb').set_trace()

        # now reverse the second half of the linked list
        nnode = node.next
        while node:
            nnnode = nnode.next # 6
            nnode.next = node # 5.next = 4
            node = nnode # 5

        # now check for the palindromes
        while node1 and node2:
            if node1.val == node2.val:
                node1 = node1.next
                node2 = node2.next
            else:
                return False
            if node1 or node2:
                return False
            return True

arr = [1,2,3,4, 5, 6]
print(arr)
head = ListNode(arr[0])
node = head
for item in arr[1:]:
    node.next = ListNode(item)
    node = node.next
sol = Solution()
print(sol.isPalindrome(head))
