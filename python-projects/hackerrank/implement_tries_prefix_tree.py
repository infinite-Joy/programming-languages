"""
208. Implement Trie (Prefix Tree)



The complexity of creating a trie is O(W*L), where W is the number of words, and L is an average length of the word: you need to perform L lookups on the average for each of the W words in the set.

Same goes for looking up words later: you perform L steps for each of the W words.

Hash insertions and lookups have the same complexity: for each word you need to check equality, which takes O(L), for the overall complexity of O(W*L).

If you need to look up entire words, hash table is easier. However, you cannot look up words by their prefix using a hash table; If prefix-based lookups are of no interest to you, use a hash table; otherwise, use a trie.

"""

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict()
        self.terminating = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children.get(ch)
        root.terminating = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for i, ch in enumerate(word):
            if ch in root.children:
                root = root.children[ch]
            else:
                return False
        if root.terminating is True:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for i, ch in enumerate(prefix):
            if ch in root.children:
                root = root.children[ch]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


trie = Trie();

trie.insert("apple");
print(trie.search("apple"));   # returns true
print(trie.search("app"));     # returns false
print(trie.startsWith("app")); # returns true
print(trie.insert("app"));
print(trie.search("app"));     # returns true
