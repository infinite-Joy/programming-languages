from collections import deque
import string

def get_children(source, words):
  # O(n)
  children = []
  words = set(words)
  letters = string.ascii_letters
  for i, ch in enumerate(source):
    for l in letters:
      new_word = source[:i] + l + source[i+1:]
      if new_word in words:
        children.append(new_word)
  return children


def bfs(source, target, words):
  # O(n)
  queue = deque([(source, 0)])
  discovered = {source: True}
  while queue:
    node, count = queue.popleft() # source, 0
    for child in get_children(node, words):
      if child == target:
        return count + 1
      if child not in discovered:
        queue.append((child, count+1))
        discovered[child] = True
  return -1


def shortestWordEditPath(source, target, words):
  """
  @param source: str
  @param target: str
  @param words: str[]
  @return: int
  """
  return bfs(source, target, words)



"""
["put", "big", "pot", "pog", "dog", "lot"]
source bit
target but




bit => but, big,




"""


