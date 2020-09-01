WRONG SOLUTION
"""

leetcode 139

https://leetcode.com/problems/word-break/

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

so what we can do is that create a trie out of the dictionary
and then starting with the first letter check if this is there in the trie
if it is not there then return false
if one branch of the trie is ending the start from the beginning
if the branch has ended without the trie being an end then also false

time complexity: O(n*m for the dictionary + n for the string)

"""

from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                nnode = TrieNode()
                node.children[ch] = nnode
                node = nnode
        node.end = True
    def search(self, word):
        node = self.root
        for ch in word:
            if node.end and len(node.children) == 0:
                node = self.root
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        # end of the word should match with the end of the trie as well
        return node.end

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        string = s
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        return trie.search(string)

# test code
string = "aaaaaaa"
word_dict = ["aaaa","aaa"]
s = Solution()
print(s.wordBreak(string, word_dict))

# the trie solution is not working out.

# according to the book they are giving the case of dynamic programming
