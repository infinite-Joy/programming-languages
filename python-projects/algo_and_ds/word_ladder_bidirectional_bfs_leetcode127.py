"""

"""

from collections import deque
from typing import List
from string import ascii_letters

class Solution:
    def explore_children(self, word, level, queue, dictionary_set):
        nwords = set()
        for i in range(len(word)):
            for ch in ascii_letters:
                nword = word[:i] + ch + word[i+1:]
                if nword != word:
                    if nword in dictionary_set:
                        nwords.add((nword, level + 1))
                        dictionary_set.remove(nword)
        queue.extend(nwords)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dictionary_set = set(wordList)
        if endWord not in dictionary_set:
            return 0
        dictionary_set.remove(endWord)

        # now will be doing a bfs
        forward_queue = deque([(beginWord, 1)])
        backward_queue = deque([(endWord, 1)])

        while forward_queue and backward_queue:
            fword, flevel = forward_queue.popleft()
            bword, blevel = backward_queue.popleft()
            print(fword, bword)
            #__import__('pdb').set_trace()
            if len(set(fword) - set(bword)) == 1:
                print(flevel, blevel)
                return flevel + blevel
            self.explore_children(fword, flevel, forward_queue, dictionary_set)
            self.explore_children(bword, blevel, backward_queue, dictionary_set)
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

