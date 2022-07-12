from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
first create the matrix and prefill the values
and then traverse in a spiral manner

"""
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # matrix initialisation
        mat = []
        for i in range(m):
            row = [-1 for _ in range(n)]
            mat.append(row)
        levels = (min(m, n) + 1) // 2
        
        for level in range(levels):
            toplimit, leftlimit = level, level
            bottomlimit, rightlimit = m-level-1, n-level-1
            
            i = toplimit
            j = leftlimit
            
            # go right
            while j < rightlimit:
                if head is None:
                    return mat
                mat[i][j] = head.val
                head = head.next
                j += 1
                
            # go down
            while i < bottomlimit:
                if head is None:
                    return mat
                mat[i][j] = head.val
                head = head.next
                i += 1
                
            # go left
            while j > leftlimit:
                if head is None:
                    return mat
                mat[i][j] = head.val
                head = head.next
                j -= 1
                
            # go up
            while i > toplimit:
                if head is None:
                    return mat
                mat[i][j] = head.val
                head = head.next
                i -= 1
                
        return mat

def spiralMatrix(m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
    # matrix initialisation
    mat = []
    for i in range(m):
        row = [-1 for _ in range(n)]
        mat.append(row)
    levels = (min(m, n) + 1) // 2
    
    for level in range(levels):
        toplimit, leftlimit = level, level
        bottomlimit, rightlimit = m-level-1, n-level-1
        
        i = toplimit
        j = leftlimit
        
        # go right
        while j < rightlimit:
            if head is None:
                return mat
            mat[i][j] = head.val
            head = head.next
            j += 1
            
        # go down
        while i < bottomlimit:
            if head is None:
                return mat
            mat[i][j] = head.val
            head = head.next
            i += 1
            
        # go left
        while j >= leftlimit:
            if head is None:
                return mat
            mat[i][j] = head.val
            head = head.next
            j -= 1
            
        # go up
        while i >= toplimit:
            if head is None:
                return mat
            mat[i][j] = head.val
            head = head.next
            i -= 1
            
    return mat
    


m = 1
n = 1
arr = [0]
def create(arr):
    head = None
    prev = None
    for elem in arr:
        node = ListNode(elem)
        if head is None:
            head = node
        if prev is not None:
            prev.next = node
        prev = node
    return head
head = create(arr)
mat = spiralMatrix(m, n, head)
print(mat)