class MinHeap:
    def __init__(self):
        self.items = []
        self.size = 0

    def build_min_heap(self, arr):
        self.items = arr
        self.size = 0
        for i in range(len(arr)-1, -1, -1):
            self.heapify_down(i)
            self.size += 1

    def heapify_down(self, i=0):
        smaller = self.left(i)
        if smaller:
            right_index = self.right(i)
            if right_index and self.items[right_index] < self.items[smaller]:
                smaller = right_index
            if self.items[i] > self.items[smaller]:
                self.swap(i, smaller)
                self.heapify_down(smaller)

    def left(self, parent):
        assert parent >= 0
        left_child = 2 * parent + 1
        if left_child < self.size:
            assert left_child > 0
            return left_child

    def right(self, parent):
        assert parent >= 0
        right_child = 2 * parent + 2
        if right_child < self.size:
            assert right_child > 0
            return right_child

    def swap(self, i, j):
        self.items[i], self.items[j] = (
            self.items[j], self.items[i])

    def pop(self):
        if self.size <= 0:
            raise StopIteration("heap is empty")
        top = self.items[0]
        last = self.items[self.size-1]
        self.items[0] = last
        self.size -= 1
        self.heapify_down()
        return top

def main(arr):
    h = MinHeap()
    h.build_min_heap(arr)
    e = 0
    while h.size>0 and e==h.pop():
        e+=1
    return e

print(main([7,1,0,3,5]))
