from collections import deque

def dfs(n, g_min_c, curr_path_c): # 0, 5, 4
  #print(n.name, g_min_c, curr_path_c)
  # base case
  if n.children == []:
    min_val = min(g_min_c, curr_path_c)
    return min_val
  # the normal case
  for child in n.children: # 5, 4
    #print('inside for loop', child.name, child.cost, curr_path_c)
    curr_path_c = curr_path_c + child.cost
    #curr_path_c += child.cost
    g_min_c = dfs(child, g_min_c, curr_path_c)
    curr_path_c = curr_path_c - child.cost
  return g_min_c

def bfs(rootNode):
    queue = deque([rootNode])
    g_min_c = 1e12
    cost_till_now = {rootNode: rootNode.cost}
    while queue:
        node = queue.popleft()
        curr_path_c = node.cost
        for child in node.children:
            queue.append(child)
            cost_till_now[child] = cost_till_now[node] + child.cost
        if node.children == []:
            g_min_c = min(g_min_c, cost_till_now[node])
    return g_min_c


def get_cheapest_cost(rootNode):
  return dfs(rootNode, 10000, 0)


##########################################
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node
class Node:

  # Constructor to create a new node
  def __init__(self, cost, name):
    self.cost = cost
    self.children = []
    self.parent = None
    self.name = name


a = Node(0, 'a')
b = Node(5, 'b')
b.parent = a
c = Node(3, 'c')
c.parent = a
d = Node(6, 'd')
d.parent = a
e = Node(1, 'e')
e.parent = c
a.children = [b,c,d]
c.children = [e]

print("dfs", get_cheapest_cost(a))
print("bfs", bfs(a))

print("#"*  10)
a = Node(0, 'a')
b = Node(5, 'a')
c = Node(4, 'a')

d = Node(3, 'a')
e = Node(2, 'a')
f = Node(1, 'a')
g = Node(1, 'a')
h = Node(0, 'a')
i = Node(10, 'a')

j = Node(6, 'a')
k = Node(1, 'a')
l = Node(5, 'a')

a.children = [b,d,j]
b.children = [c]
d.children = [e, h]
h.children = [i]
e.children = [f]
f.children = [g]
j.children = [k,l]

print('dfs', get_cheapest_cost(a))
print("bfs", bfs(a))
