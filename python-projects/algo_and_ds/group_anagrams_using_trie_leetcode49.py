"""

group  anagrams leet code 49

https://leetcode.com/problems/group-anagrams/

so what we can do is that, sort all the strings in the arr.

and then create a trie

and when building the trie we can see if they are already present in the trie
if present then this is an anagram else build the trie

"""

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string, groups, identifier):
        node = self.root
        match = True
        for ch in string:
            if ch in node.children:
                node = node.children[ch]
            else:
                match = False
                nnode = TrieNode()
                node.children[ch] = nnode
                node = nnode

        if match is True and node.end is True: # anagram found
            groups[string].append(identifier)
        if match is False: # went on some other route, new group
            groups[string] = [identifier]
        # remaining conds are somewhere in the middle
        node.end = True

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1: return [strs]

        strings = strs
        strings = ["".join(sorted(s)) for s in strings]
        groups = {}
        trie = Trie()

        for idx, string in enumerate(strings):
            if string == "":
                if "empty_string" not in groups:
                    groups["empty_string"] = []
                groups["empty_string"].append(idx)
            else:
                trie.insert(string, groups, idx)
            print(groups)

        return [[strs[i] for i in group] for base, group in groups.items()]



# test case

strs = ["eat","tea","tan","ate","nat","bat"]
s = Solution()
#print(s.groupAnagrams(strs))

strs = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]
s = Solution()
print(s.groupAnagrams(strs))


# a simpler solution can probably be done using hashmaps

# put the strings into the  hashmap and just see if the they are the same


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1: return [strs]

        strings = strs
        strings = ["".join(sorted(s)) for s in strings]
        groups = defaultdict(list)

        for idx, string in enumerate(strings):
            if string == "":
                groups["empty_string"].append(idx)
            else:
                groups[string].append(idx)
        return [[strs[i] for i in group] for base, group in groups.items()]

strs = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]
s = Solution()
print(s.groupAnagrams(strs))
