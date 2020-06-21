from collections import defaultdict
from collections import Counter
from collections import deque
from typing import Tuple, Optional

def check_gene_config(string):
    nums = len(string) / 4
    counts = Counter(string)
    return all([v == nums for k, v in counts.items()])

print(check_gene_config("ACTGACTG"))
print(check_gene_config("GTTCCGAA"))

all_values = set("GACT")


class Graph:

    def __init__(self, root):
        self._graph = defaultdict(list)
        self._root = root

    def add_vertex(self, e, *vertices):
        if self._root is None:
            self._root = e
        for v in vertices:
            self._graph[e] = v

    def explore_children_space(self, v, curr_idx):
        fixed_values = self.get_difference(v)
        for change_idx in range(curr_idx, len(v)):
            if change_idx not in fixed_values:
                current_config = v[change_idx]
                remainin_config = all_values - set(current_config)
                new_possibles = v
                for value in remainin_config:
                    new_possibles = v[:change_idx] + value + v[change_idx+1:]
                    self._graph[v].append(new_possibles)

    def get_difference(self, v):
        differences = []
        return [i for i, ch in enumerate(v) if self._root[i] != ch]

    def bfs(self, start=None):
        if start is None:
            start = self._root
        queue = deque([start])
        level = {start: 0}
        parent = {start: None}
        while queue:
            v = queue.popleft()
            if check_gene_config(v):
                return parent, v
            self.explore_children_space(v, level[v])
            for child in self._graph[v]:
                if child not in level:
                    queue.append(child)
                    level[child] = level[v] + 1
                    parent[child] = v

    def find_shortest_path(self):
        shortest_path = []
        parents, end = self.bfs(self._root)
        shortest_path.append(end)
        curr_node = end
        while parents[curr_node]:
            curr_node = parents[curr_node]
            shortest_path.append(curr_node)
        return shortest_path


g = Graph("ACTGAAAG")
g.explore_children_space(g._root, 1)
print(g._graph)
print(g.get_difference("AGTGAAAA"))
#print(g.bfs())
print(g.find_shortest_path())
