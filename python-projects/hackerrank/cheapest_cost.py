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

print(get_cheapest_cost(a))
