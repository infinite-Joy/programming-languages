##########################################################
# CODE INSTRUCTIONS:                                     #
# 1) The method findLargestSmallerKey you're asked       #
#    to implement is located at line 30.                 #
# 2) Use the helper code below to implement it.          #
# 3) In a nutshell, the helper code allows you to        #
#    to build a Binary Search Tree.                      #
# 4) Jump to line 71 to see an example for how the       #
#    helper code is used to test findLargestSmallerKey.  #
##########################################################

"""

num 22

25.left = 21

bs:
  if n less: go left
  else go right

  low, high = 21, 25


if going left (high.left == low):
  then find the rightmost value of low
    that is less than num


if going right (low.right == high):
  just returning the left node

the first algo did not work out correctly

time complexity: O(logn)
space complexity: O(1)


"""



# A node
class Node:

# Constructor to create a new node
  def __init__(self, key):
      self.key = key
      self.left = None
      self.right = None
      self.parent = None


# A binary search tree
class BinarySearchTree:

  # Constructor to create a new BST
  def __init__(self):
      self.root = None

  def bin_search(self, num, root, minval):
    # num = 10
    if num == root.key:
      return root
    if root.right is not None and num > root.key:
      minval = min(minval, root.right.key)
      return self.bin_search(num, root.right, minval)
    if root.left is not None and num < root.key:
      minval = min(minval, root.left.key)
      return self.bin_search(num, root.left, minval)
    else:
      return minval

  def find_largest_smaller_key(self, num):
    root = self.root
    maxval = -1
    while root:
      if num <= root.key:
        root = root.left
      else:
        maxval = root.key
        root = root.right
    return maxval


  # Given a binary search tree and a number, inserts a
  # new node with the given number in the correct place
  # in the tree. Returns the new root pointer which the
  # caller should then use(the standard trick to avoid
  # using reference parameters)
  def insert(self, key):

      # 1) If tree is empty, create the root
      if (self.root is None):
          self.root = Node(key)
          return

      # 2) Otherwise, create a node with the key
      #    and traverse down the tree to find where to
      #    to insert the new node
      currentNode = self.root
      newNode = Node(key)

      while(currentNode is not None):
        if(key < currentNode.key):
          if(currentNode.left is None):
            currentNode.left = newNode
            newNode.parent = currentNode
            break
          else:
            currentNode = currentNode.left
        else:
          if(currentNode.right is None):
            currentNode.right = newNode
            newNode.parent = currentNode
            break
          else:
            currentNode = currentNode.right

#########################################
# Driver program to test above function #
#########################################

bst  = BinarySearchTree()

# Create the tree given in the above diagram
bst.insert(20)
bst.insert(9);
bst.insert(25);
bst.insert(5);
bst.insert(12);
bst.insert(11);
bst.insert(14);

result = bst.find_largest_smaller_key(17)

print ("Largest smaller number is %d " %(result))

result = bst.find_largest_smaller_key(10)

print ("Largest smaller number is %d " %(result))

result = bst.find_largest_smaller_key(22)

print ("Largest smaller number is %d " %(result))


result = bst.find_largest_smaller_key(4)

print ("Largest smaller number is %d " %(result))
