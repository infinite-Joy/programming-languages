class MinIntHeap:

    def __init__(self):
        self._items = []

    @property
    def size(self):
        return len(self._items)

    def get_left_child_index(self, parent_index):
        return 2 * parent_index + 1

    def get_right_child_index(self, parent_index):
        return 2 * parent_index + 2

    def get_parent_index(self, child_index):
        return (child_index - 1) // 2

    def has_left_child(self, parent_index):
        left = self.get_left_child_index(parent_index)
        return left < self.size

    def has_right_child(self, parent_index):
        return self.get_right_child_index(parent_index) < self.size

    def has_parent(self, child_index):
        if child_index >= self.size:
            raise ValueError(
                "index {} not part of the heap".format(child_index))
        # only the first element will not have a parent
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

    def parent(self, child_index):
        if child_index == 0:
            ValueError("this is the first element and has no parent")
        parent_index = self.get_parent_index(child_index)
        return self._items[parent_index]

    def swap(self, index1, index2):
        self._items[index1], self._items[index2] = (
            self._items[index2], self._items[index1])

    def raise_error_if_no_elements(self):
        if self.size == 0:
            raise ValueError(
                "No elements in the heap. "
                "Add some element using the add method")

    def peek(self):
        self.raise_error_if_no_elements()
        return self._items[0]

    def poll(self):
        self.raise_error_if_no_elements()
        last_elem = self._items.pop()

        # if there is only one element then the operation is simple.
        if self.size == 0:
            return last_elem
        # make the last element the first element
        first_elem = self._items[0]
        self._items[0] = last_elem
        # now heapify down the DS
        self.heapify_down()
        return first_elem

    def add(self, item):
        self._items.append(item)
        if self.size > 1:
            self.heapify_up()
        return self

    def heapify_up(self):
        # start from the end
        index = self.size - 1
        while self.has_parent(index) and self.parent(index) > self._items[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def heapify_down(self):
        # start from the top
        index = 0
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index):
                right_child = self.get_right_child(index)
                if right_child < self.get_left_child(index):
                    smaller_child_index = self.get_right_child_index(index)
            if self._items[index] >= self._items[smaller_child_index]:
                self.swap(index, smaller_child_index)
                index = smaller_child_index
            else:
                return


from random import shuffle
from functools import reduce

arr = list(range(15))
shuffle(arr)
print("shuffled arr", arr)
heap = MinIntHeap()
heap = reduce(lambda h, x: h.add(x), arr, heap)
print(heap._items)

print("finding the kth smallest element")
for i in range(7):
    kth_smallest = heap.poll()
print(kth_smallest)
