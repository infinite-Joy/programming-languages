"""

https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

maxumum xor of two numbers using tries

[3, 10, 5, 25, 2, 8]

3 = 11
10 = 1010
5 = 101

what i am thinkign right now is

                *
            /       \
        0               1
          \            /    \
            1        0         1
           /           \
          0             1
            \
             1

the maximum xor is the root left ^ root right

25 2 8

                    *
                /
            0                 1
              \             /
                1        0
                       /
                    0

                        1

                            1

complexity: O(n)
since the maximum result is 2**31 hence the log term will not come into play
the space complexity is O(n)

the above algo is not working
will need to change it based on the recommendations of the internet

basically start from the end and get all the numbers

"""

from math import inf
class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = [None, None] # can be either 0 or 1
        self.end = False
    def __repr__(self):
        return "{}".format(self.val)
class Trie:
    def __init__(self):
        self.root = TrieNode('*')
    def add_val(self, num):
        node = self.root
        for i in range(31, -1, -1):
            val = (num >> i) & 1
            nnode = node.children[val]
            if nnode is None:
                nnode = TrieNode(val)
                node.children[val] = nnode
            node = nnode
            num -= val << i
    def find_opp(self, num):
        node = self.root
        opp = 0
        for i in range(31, -1, -1):
            val = (num >> i) & 1
            nnode = node.children[~val]
            if nnode is None:
                nnode = node.children[val]
            node = nnode
            num -= val << i
            opp = (opp << 1) + node.val
        return opp
def find_max_xor(arr, trie):
    max_xor = -inf
    for num in arr:
        opp = trie.find_opp(num)
        max_xor = max(max_xor, num ^ opp)
    return max_xor
def main(arr):
    if len(arr) in (0, 1): return 0

    trie = Trie()
    for num in arr:
        trie.add_val(num)

    return find_max_xor(arr, trie)


# test cases
arr = [3, 10, 5, 25, 2, 8]
print(arr)
print(main(arr))

arr = []
print(arr)
print(main(arr))

arr = [3]
print(arr)
print(main(arr))
