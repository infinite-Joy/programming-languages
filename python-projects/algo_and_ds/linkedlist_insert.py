#!/bin/python3
# https://www.hackerrank.com/test/61sq9qfa63d/questions/et5sd436k19

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)



# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    # this can be dont in O(n) time
    node = head
    for i in range(position-1):
        node = node.next

    foll_elem = node.next
    data = SinglyLinkedListNode(data)
    data.next = foll_elem
    node.next = data

    return head

if __name__ == '__main__':
