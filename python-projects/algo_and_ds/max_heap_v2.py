"""
https://www.youtube.com/watch?v=Q_eia3jC9Ts&t=341s

building the max heap

for the heaping method only the non heap elements need to be build. 

leaf elements are floor(n) + 1 to n

start the buildup heapify from the non leaf element

"""

import math

class MaxHeap:
    def __init__(self, arr=None, method='builddown'):
        # self.arr = arr if arr is not None else []
        if method == 'builddown':
            self.arr = self.builddown(arr)
        else:
            self.arr = self.buildup(arr)

    def builddown(self, arr):
        for item in arr:
            self.arr = self.insert(item)
        return self.arr

    def __len__(self):
        return len(self.arr)

    def __bool__(self):
        return bool(len(self))

    def get_children(self, i):
        li = 2*i
        ri = 2*(i+1)
        if li >= len(self.arr):
            left_val = self.arr[2*i]
        else:
            left_val = None
        if ri >= len(self.arr):
            right_val = self.arr[2*(i+1)]
        else:
            right_val = None
        return li, ri, left_val, right_val

    def get_parent(self, i):
        p = math.floor(i/2)
        return p, self.arr[p] if p >= 0 else None, None
    
    def insert(self, el):
        self.arr.append(el)
        if len(self.arr) == 1:
            return self.arr
        return self.heapify_up(self.arr)

    def heapify_up(self, arr):
        curr_indx = len(arr) - 1
        curr_val = arr[curr_indx]
        parent, parent_val = self.get_parent(curr_indx)
        while parent_val and parent_val < curr_val:
            self.arr[parent], self.arr[curr_indx] = curr_val, parent_val
            curr_indx = parent
            parent, parent_val = self.get_parent(curr_indx)
        return self.arr


    # def buildup(self, arr):

    # def delete(self, i):