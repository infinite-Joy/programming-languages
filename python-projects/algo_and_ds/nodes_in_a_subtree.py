import math
# Add any extra import statements you may need here


class Node: 
  def __init__(self, data): 
    self.val = data 
    self.children = []

# Add any helper functions you may need here

"""
go through the node
basically go through the arr and put the nodes as per the postition in the list.
then based on the position there are we can jump to the node directly and then do the counting of the leaves of the tree
"""

from collections import deque

def build_nodes(root, s):
    queue = deque([root])
    nodes = [None] * (len(s) + 1)
    while queue:
        node = queue.popleft()
        val = node.val
        nodes[val] = node
        for child in node.children:
            queue.append(child)
    return nodes

def query(node, q, s):
  this_count = int(s[node.val-1] == q)
  # print(this_count)
  for child in node.children:
    this_count += query(child, q, s)
    # print('this_count', this_count)
  return this_count


def count_of_nodes(root, queries, s):
    # Write your code here
    # print(s)
    nodes = build_nodes(root, s)
    # print(nodes)
    output = []
    for val, q in queries:
      # print('query', val, q)
      node = nodes[val]
      # print(node)
      output.append(query(node, q, s))
    return output
    
    
# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
      if i != 0:
          print(', ', end='')
      print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
      result = False
  for i in range(min(expected_size, output_size)):
      result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1
    
if __name__ == "__main__":

  # Testcase 1
  n_1 ,q_1 = 3, 1 
  s_1 = "aba"
  root_1 = Node(1) 
  root_1.children.append(Node(2)) 
  root_1.children.append(Node(3)) 
  queries_1 = [(1, 'a')]

  output_1 = count_of_nodes(root_1, queries_1, s_1)
  expected_1 = [2]
  check(expected_1, output_1)

  # Testcase 2
  n_2 ,q_2 = 7, 3 
  s_2 = "abaacab"
  root_2 = Node(1)
  root_2.children.append(Node(2))
  root_2.children.append(Node(3))
  root_2.children.append(Node(7))
  root_2.children[0].children.append(Node(4))
  root_2.children[0].children.append(Node(5))
  root_2.children[1].children.append(Node(6))
  queries_2 = [[1, 'a'],[2, 'b'],[3, 'a']]
  output_2 = count_of_nodes(root_2, queries_2, s_2)
  expected_2 = [4, 1, 2]
  check(expected_2, output_2)

  # Add your own test cases here