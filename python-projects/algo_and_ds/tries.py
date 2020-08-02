# -*- coding: utf-8 -*-

from typing import Set

class Trie:
    class _TrieNode:

        def __init__(self, ch: str):
            self.char = ch
            self.children = {}
            self.occurence_count = 0
            self.end_of_word: bool = False

        def __repr__(self):
            return "trie node: {}, {}, {}, {}".format(self.char, self.children, self.occurence_count, self.end_of_word)

        def __str__(self):
            return repr(self)

    def __init__(self):
        self._root = self._TrieNode("*")

    def add_word(self, word):
        curr_node = self._root
        for ch in word:
            if ch == curr_node.char:
                curr_node.occurence_count += 1
            elif ch in curr_node.children:
                curr_node = curr_node.children[ch]
                curr_node.occurence_count += 1
            else:
                node = self._TrieNode(ch)
                curr_node.children[ch] = node
                curr_node.occurence_count += 1
                curr_node = node
        curr_node.end_of_word = True

    def find_prefix(self, word, node=None):
        if node is None:
            node = self._root
        if word == "":
            return node
        ch = word[0]
        if ch == node.char:
            return self.find_prefix(word[1:], node)
        if ch in node.children:
            return self.find_prefix(word[1:], node.children[ch])
        else:
            return None

    def print_tree(self):
        print(repr(self._root))


tn = Trie()
tn.add_word("add")
tn.add_word("delete")
tn.print_tree()
print(tn.find_prefix("add"))
print(tn.find_prefix("del"))
print(tn.find_prefix("delt"))
