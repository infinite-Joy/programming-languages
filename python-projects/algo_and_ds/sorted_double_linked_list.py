#!/bin/python3

# https://www.hackerrank.com/test/61sq9qfa63d/questions/5tck2fhk6rl

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node):
    while node:
        print(str(node.data), end='->')

        node = node.next


# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    # we can just iterate on the ll
    # and then whenever we get the value smaller than
    # current then we do prev.next = datat
    # and data.next = node
    node = head
    prev = head.prev if head else None

    while node is not None and node.data < data:
        prev = node
        node = node.next

    data = DoublyLinkedListNode(data)
    __import__('pdb').set_trace()
    if node is None:
        if prev is not None:
            prev.next = data
            data.prev = prev
            return head
        else:
            return data
    else:
        if prev is not None:
            prev.next = data
        else:
            head = data
        data.next = node
        node.prev = data
        data.prev = prev
        return head


if __name__ == '__main__':
    t = 1
    llist_count = 3
    llist = DoublyLinkedList()
    llist.insert_node(2)
    llist.insert_node(3)
    llist.insert_node(4)

    llist1 = sortedInsert(llist.head, 1)

    print_doubly_linked_list(llist.head)
