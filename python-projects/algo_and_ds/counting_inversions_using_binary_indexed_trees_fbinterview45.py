# in this we will be using binary indexed trees
# the time complexity of this is O(n)

# fenwick trees are good for finding the prefix sum of arrays
# if there are updates to the array then this will take that much time for the
# normal method. hence fenwick trees are better.

# this implementation will take O(nlog(max(arr)))

class Bit:
    def __init__(self, n):
        self.data = [0] * (n+1)
        self.size = len(self.data)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & (-i)
        return s

    def add(self, i, val):
        while i < self.size:
            self.data[i] += val
            i += i & (-i)


def inversion(arr):
    print(arr)
    res = 0
    bit = Bit(max(arr))
    for i, elem in enumerate(arr):
        res += i - bit.sum(elem)
        bit.add(elem, 1)
        print(bit.data)
    return res


arr = [2,1,3,1,2]
print(inversion(arr))

#arr = [8, 22, 7, 9, 31, 19, 5, 13]
#print(countInversions_merge_sort(arr))
