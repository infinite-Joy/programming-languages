"""
https://leetcode.com/problems/map-sum-pairs/

so basically we can trying creating the trie for this
and then for each prefix do a depth first search and see all the values and then do the sum of all the values

time complexity: O(n*m)

"""

class TrieNode:
    def __init__(self, ch):
        self.ch = ch
        self.children = {}
        self.val = 0
class MapSum: # this is the trie
    def __init__(self):
        self.root = TrieNode("*")
        self.total = 0
    def insert(self, key: str, val: int) -> None:
        node = self.root
        for ch in key:
            nnode = node.children.get(ch)
            if nnode is None:
                nnode = TrieNode(ch)
                node.children[ch] = nnode
            node = nnode
        node.val = val
    def dfs(self, root):
        if root is None:
            return
        self.total += root.val
        for _, child_node in root.children.items():
            self.dfs(child_node)
    def sum(self, prefix: str) -> int:
        self.total = 0
        node = self.root
        for ch in prefix:
            nnode = node.children.get(ch)
            if nnode is None: return 0
            node = nnode
        self.dfs(node)
        return self.total

# test cases
ms = MapSum()
ms.insert("apple", 3)
print(ms.sum("ap"))
ms.insert("app", 2)
print(ms.sum("ap"))


ms = MapSum()
ms.insert("a", 3)
print(ms.sum("ap"))
ms.insert("b", 2)
print(ms.sum("a"))
