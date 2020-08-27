"""

https://leetcode.com/problems/replace-words/

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

algo:

create a trie out of the dictionary
then we can go through the sentence word  by word and see which trie is matching
once if the trie is matching then we can replace that word in the sentence

time complecity: O(|dictionary|*|max(dictionary)| + |max(dictionary)|*|words|)
space complexity: O(dictionary + words)
    i cannot go beyond this because we are not doing the replacement in place
    and returning the sentence
    in any case changin ght sentence is immutable hence this will be O(n)

                        *
                c       b       r
                a       a       a
                t       t       t

"""

from collections import defaultdict

class TrieNode:
    def __init__(self, ch):
        self.ch = ch
        self.children = {}
        self.eow = False
class Trie:
    def __init__(self):
        self.root = TrieNode('*')
    def add_word(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                nnode = TrieNode(ch)
                node.children[ch] = nnode
            else:
                nnode = node.children[ch]
                # i have come this path before
                if nnode.eow is True:
                    return self
            node = nnode
        node.eow = True
        return self
    def search(self, word):
        node = self.root
        builder = ""
        for ch in word:
            if ch in node.children:
                nnode = node.children[ch]
                builder += ch
                if nnode.eow is True:
                    return builder
            else:
                return word
            node = nnode

from typing import List
from functools import reduce

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()

        # build the trie
        trie = reduce(lambda trie, word: trie.add_word(word), dictionary, trie)

        roots = []
        for word in sentence.split():
            root = trie.search(word)
            roots.append(root)

        return " ".join(roots)


dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
s = Solution()
print(s.replaceWords(dictionary, sentence))

dictionary = ["a","b","c"]
sentence = "aadsfasf absbs bbab cadsfafs"
print(s.replaceWords(dictionary, sentence))

dictionary = ["a", "aa", "aaa", "aaaa"]
sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
print(s.replaceWords(dictionary, sentence))

dictionary = ["catt","cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
print(s.replaceWords(dictionary, sentence))

dictionary = ["ac","ab"]
sentence = "it is abnormal that this solution is accepted"
print(s.replaceWords(dictionary, sentence))
