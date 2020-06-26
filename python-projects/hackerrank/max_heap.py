class MaxHeap:

    def __init__(self):
        self._items = []
        self._size = 0

    def get_left_child_index(self, parent_index):
        return 2 * parent_index + 1

    def get_right_child_index(self, parent_index):
        return 2 * parent_index + 2

    def get_parent_index(self, child_index):
        return (child_index - 1) // 2

    def has_left_child(self, parent_index):
        left = self.get_left_child_index(parent_index)
        return left < self._size

    def has_right_child(self, parent_index):
        right = self.get_right_child_index(parent_index)
        return right < self._size

    def has_parent(self, child_index):
        if child_index > self._size:
            raise ValueError(
                "child not part of the heap")
        if child_index == 0:
            return False
        return True

    def get_left_child(self, parent_index):
        if self.has_left_child(parent_index):
            left_child_index = self.get_left_child_index(parent_index)
            return self._items[left_child_index]

    def get_right_child(self, parent_index):
        if self.has_right_child(parent_index):
            right_child_index = self.get_right_child_index(parent_index)
            return self._items[right_child_index]

    def get_parent(self, child_index):
        if self.has_parent(child_index):
            parent_index = self.get_parent_index(child_index)
            return self._items[parent_index]

    def swap(self, index1, index2):
        self._items[index1], self._items[index2] = (
            self._items[index2], self._items[index1]
        )

    def peek(self):
        return self._items[0]

    def raise_error_if_no_elements(self):
        if self._size == 0:
            raise ValueError("Heap is empty")

    def poll(self):
        """
        We need to get the element as well as remove the elemnt
        """
        self.raise_error_if_no_elements()
        last_elem = self._items.pop()
        self.size -= 1

        # if there is only one element then the operation is simple.
        if self.size == 1:
            return

        # make the last element the first element
        first_elem = self._items[0]
        self._items[0] = last_elem
        # now heapify down the DS
        self.heapify_down()
        return first_elem

    def inplace_sort(self):
        self.raise_error_if_no_elements()
        while self._size > 1:
            # swap the first and last element in place
            self._items[0], self._items[self._size-1] = (
                self._items[self._size-1], self._items[0])
            # our heap has not reduced, plus this is not a valid heap
            self._size -= 1
            # so we heapify it
            self.heapify_down()

    def add(self, item):
        self._items.append(item)
        self._size += 1
        if self._size > 1:
            self.heapify_up()
        return self

    def heapify_up(self):
        # start from the last
        index = self._size - 1
        while self.has_parent(index) and self.get_parent(index) < self._items[index]:
            parent_index = self.get_parent_index(index)
            self.swap(parent_index, index)
            index = parent_index

    def heapify_down(self, index=0):
        if self.has_left_child(index):
            larger_child_index = self.get_left_child_index(index)
            if self.has_right_child(index):
                right_child = self.get_right_child(index)
                if right_child > self.get_left_child(index):
                    larger_child_index = self.get_right_child_index(index)
            if self._items[index] <= self._items[larger_child_index]:
                self.swap(index, larger_child_index)
                self.heapify_down(larger_child_index)

    def build_max_heap(self, elements):
        self._items = elements
        start = len(elements) - 1
        for j in range(start, -1, -1):
            print(self._size)
            self.heapify_down(j)
            self._size += 1

from random import shuffle, randint

from functools import reduce

arr = list(range(15))
shuffle(arr)
print("shuffled arr", arr)
heap = MaxHeap()
heap = reduce(lambda h, x: h.add(x), arr, heap)
print(heap._items)

heap.inplace_sort()
print(heap._items)

import heapq

print("using heapq")
arr = list(range(15))
shuffle(arr)
print("shuffled arr", arr)
heap = heapq.heapify(arr)

def heapsort(arr):
    return [heapq.heappop(arr) for i in range(len(arr))]

__import__('pprint').pprint(arr)
print(heapsort(arr))

print("Bottom-Up Heap Construction")
arr = list(range(15))
shuffle(arr)
print("shuffled arr", arr)
heap = MaxHeap()
heap.build_max_heap(arr)
print("current hea[", heap._items)
heap.inplace_sort()
print("after sprting", heap._items)
