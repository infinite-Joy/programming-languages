"""

design and add words datastructure

leetcode 211

this looks like it can be done with a trie

    something like build a trie

    b -> a -> d
    d -> a -> d

    if there are dots

    if ch is . then for loop on all the children and then do a bfs

    if not a . So basically have a queue


"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

from collections import deque

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                nnode = TrieNode()
                node.children[ch] = nnode
                node = nnode
        node.end = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        queue = deque([(self.root, 0)])
        while queue:
            print(queue)
            node, pos = queue.popleft()
            if pos >= len(word):
                return True
            if word[pos] == '.':
                queue.extend([(n, pos+1) for n in node.children.values()])
            else:
                print(word[pos], node.children)
                if word[pos] in node.children:
                    ch = word[pos]
                    child = node.children[ch]
                    queue.append((child, pos + 1))
                else:
                    return False


wordDictionary = WordDictionary()
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); # return False
wordDictionary.search("bad"); #return True
wordDictionary.search(".ad"); #return True
wordDictionary.search("b.."); #return True
