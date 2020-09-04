"""

word ladder

https://leetcode.com/problems/word-ladder/

at worst this is the is going to be O(size)

the bruteforce for this is

change a letter of a word
if word does not match end word for each word in the dict see if this is the same as the that word
buid a tree in that manner. also store the levels
if match is there return the level. since this is bfs hence the first time we get this we will return the solution

start -> 26*D -> 26*D since they are the same length

D**D

we can make it a hashmap so this becomes 26**D complexity with space being O(D)

still this is not good.

"hit" -> "hot" -> "dot" -> "dog" -> "cog"

maybe i can use dp to this

    c   o   g
h
i
t

can i use  a trie to break the dictionary up

                    h       d       l       c
                    o       o       o       o
                    t     t  g    t   g     g

maybe something like edit distance  between the different words in the dictionary and then assign them the edit distance and then sort based on that
that is like nlogn

then i can go ahead with the earlier algo but not required to go through all of them. this will become O(n)

    hot     dot
            lot

lets go ahead with this and then will see the dp solution

time complexity using bfs O(b*d)


"""

from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        there = None
        for word in wordList:
            if endWord == word:
                there = True
        if not there:
            return 0

        dictionary_set = set(wordList)

        # now will be doing a bfs
        queue = deque([(beginWord, 1)])
        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level
            word_set = set(word)
            dictionary_set_cp = {i for i in dictionary_set}
            for nword in dictionary_set_cp:
                if len(word_set.difference(set(nword))) == 1:
                    queue.append((nword, level + 1))
                    dictionary_set.remove(nword)
        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
sol = Solution()
print(sol.ladderLength(beginWord, endWord, wordList))

# this will not work as there would be a solt
# this is not working out

"leet"
"code"
["lest","leet","lose","code","lode","robe","lost"]

