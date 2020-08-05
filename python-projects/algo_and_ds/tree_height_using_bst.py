# https://www.hackerrank.com/test/61sq9qfa63d/questions/6509o4gn0nd

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break



# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''
# this needs to be done as a bfs
# time complexity: O(n)
# space complexity: O(n)

from collections import deque

def height(root):
    queue = deque([(root, 0)])
    max_height = 0
    while queue:
        node, height = queue.popleft()
        max_height = max(max_height, height)
        if node.left is not None:
            queue.append((node.left, height+1))
        if node.right is not None:
            queue.append((node.right, height+1))
    return max_height




