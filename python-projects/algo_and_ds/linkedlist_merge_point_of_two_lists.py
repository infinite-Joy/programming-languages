#!/bin/python3
# https://www.hackerrank.com/test/61sq9qfa63d/questions/dacmkl81koq

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



# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    # since they are merging i can have two lists
    # we can create two arrays with the pointers to the nodes
    # and once we see that the two nodes are diverging then we can see that the
    # next node is the merging point
    # time complexity: O(n+m)
    # space complexity: O(n+m)

    arr1 = []
    node = head1
    while node:
        arr1.append(node)
        node = node.next

    arr2 = []
    node = head2
    while node:
        arr2.append(node)
        node = node.next

    len1 = len(arr1) - 1
    len2 = len(arr2) - 1

    # if any of them do not have values there is no point in going forward.
    if len1 == 0:
        return arr1[0].data
    if len2 == 0:
        return arr2[0].data

    while len1 >= 0 and len2 >= 0:
        if arr1[len1] is arr2[len2]:
            if len1 > 0:
                len1 -= 1
            if len2 > 0:
                len2 -= 1
        else:
            # print(arr1[len1+1].data)
            return arr1[len1+1].data
    # since we have traversed the whole array and they are all the same then we
    # just return the first element
    return arr1[0].data

