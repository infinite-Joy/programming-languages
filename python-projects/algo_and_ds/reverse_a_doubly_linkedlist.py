#!/bin/python3

# https://www.hackerrank.com/test/61sq9qfa63d/questions/17k820n7296

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

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)



# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    # first go to the end
    node = head
    while node.next is not None:
        node = node.next
    # 1->2->3->4->5->None
    #

    head = node
    # print(head)
    prevval = node.next
    while node is not None: # 5
        # print(node.data)
        nextval = node.prev # 4
        node.prev = prevval # 5 <- None
        node.next = nextval # 5 -> 4
        prevval = node # 5
        node = node.next # 4
    return head
    # return head

    # we will probably need to keep the current.

