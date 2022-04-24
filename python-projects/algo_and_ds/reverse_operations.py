import math
# Add any extra import statements you may need here


"""
implementation of the linked list


"""


class Node:
  def __init__(self, x):
    self.data = x
    self.next = None

# Add any helper functions you may need here

"""
for this in any case need to go over the linked list

need to do in a single pass

curr start

loop elem:
    if curr even and start not found: define curr start
    till even: curr end
    if odd: run while loop and reverse and link
    time complexity: O(n)
    but space complexity : O(1) not considering the space taken up by the list.
"""

def reverse_even(start, end):
    node = start
    prev = None
    next = None
    while node and node != end:
        # 1 -> 2 -> 3 => 1 <- 2 3
        next = node.next
        node.next = prev
        node = next
    # return head, tail
    return end, start



def reverse(head):
    # Write your code here
    odd_end = None
    even_start = None
    even_end = None
    odd_start = None
    prev = None
    new_head = head
    node = head
    while node:
        if node == head:
            pass
        # previous is odd and now is even
        elif prev.val % 2 == 1 and node.val % 2 == 0:
            even_start = node
            odd_end = prev
        elif (even_start and node is None) or (prev.val % 2 == 0 and node.val % 2 == 1):
            even_end = prev
            odd_start = node
            even_start, even_end = reverse_even(even_start, even_end)
            if odd_end:
                odd_end.next = even_start
            even_end.next = odd_start
            odd_end, even_start, even_end, odd_start = [None] * 4


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printLinkedList(head):
  print('[', end='')
  while head != None:
    print(head.data, end='')
    head = head.next
    if head != None:
      print(' ', end='')
  print(']', end='')

test_case_number = 1

def check(expectedHead, outputHead):
  global test_case_number
  tempExpectedHead = expectedHead
  tempOutputHead = outputHead
  result = True
  while expectedHead != None and outputHead != None:
    result &= (expectedHead.data == outputHead.data)
    expectedHead = expectedHead.next
    outputHead = outputHead.next

  if not(outputHead == None and expectedHead == None):
    result = False

  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', sep='', end='')
    printLinkedList(tempExpectedHead)
    print(' Your output: ', end='')
    printLinkedList(tempOutputHead)
    print()
  test_case_number += 1

def createLinkedList(arr):
  head = None
  tempHead = head
  for v in arr:
    if head == None:
      head = Node(v)
      tempHead = head
    else:
      head.next = Node(v)
      head = head.next
  return tempHead

if __name__ == "__main__":
  head_1 = createLinkedList([1, 2, 8, 9, 12, 16])
  expected_1 = createLinkedList([1, 8, 2, 9, 16, 12])
  output_1 = reverse(head_1)
  check(expected_1, output_1)

  head_2 = createLinkedList([2, 18, 24, 3, 5, 7, 9, 6, 12])
  expected_2 = createLinkedList([24, 18, 2, 3, 5, 7, 9, 12, 6])
  output_2 = reverse(head_2)
  check(expected_2, output_2)

  # Add your own test cases here
  