# Definition for a Node.
# how to clone a graph using dfs
# since this is dfs complexity is O(V+E)

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    discovered = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node not in self.discovered:
            new_node = Node(node.val)
            self.discovered[node] = new_node
        else:
            new_node = self.discovered[node]
        for neighbor in node.neighbors:
            if neighbor in self.discovered:
                new_neighbor = self.discovered[neighbor]
                new_node.neighbors.append(new_neighbor)
            else:
                new_neighbor = Node(neighbor.val)
                new_node.neighbors.append(new_neighbor)
                self.discovered[neighbor] = new_neighbor
                self.cloneGraph(neighbor)

        return  new_node


