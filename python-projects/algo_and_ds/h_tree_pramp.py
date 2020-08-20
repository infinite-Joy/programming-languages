from math import sqrt

def drawLine(a, b):
  print(a, b)

def helper(x, y, length):
  # the middle dash
  a = (x, y - length/2)
  b = (x, y + length/2)
  drawLine(a, b)

  # the left dash
  a = (x - length/2, y - length/2)
  b = (x + length/2, y - length/2)
  drawLine(a, b)

  # the right dash
  a = (x - length/2, y + length/2)
  b = (x + length/2, y + length/2)
  drawLine(a, b)
  print('#####################')


def recur(x, y, length, depth, currdepth=1):
  helper(x, y, length)

  if currdepth == depth:
    return

  # top left
  recur(x - length/2, y - length/2, length/sqrt(2), depth, currdepth+1)

  # bottom left
  recur(x + length/2, y - length/2, length/sqrt(2), depth, currdepth+1)


  # bottom right
  recur(x + length/2, y + length/2, length/sqrt(2), depth, currdepth+1)

  # top right
  recur(x - length/2, y + length/2, length/sqrt(2), depth, currdepth+1)


recur(0, 0, 1, 2)



"""

5 times drawlines

0 0, 1, 1


topleft = -1, 1, root2, 1
do recursion

bottomleft = -1, -1, root2, 1
do recursion

bottomright = -1, 1, root2, 1
do recursion

topright = 1, 1, root2, 1
do recursion

time complexity: O(4**n) where n = depth
space complexity: O(n)


"""
