# Graph coloring problem is to assign colors to elements of a graph subject to
# certain constraints.
# Vertex coloring is the most common graph coloring problem. The problem is
# given m colors find a way of coloring the vertices of the graph, such that no
# two adjacent vertices are colored using the same color.

# the smallest number of colors needed to color a graph is called its chromatic
# number.

# greedy algorithm:
# color first vertex with first color.
# for the following V-1 vertices, consider the currently picked vertex and
# color and color it with the lowest numbered color that has not been used in
# the adjacent vertices. if all previously used color appear on vertex v,
# assign a new color to it.

# There can be many more applications: For example the below reference video lecture has a case study at 1:18.
# Akamai runs a network of thousands of servers and the servers are used to
# distribute content on Internet. They install a new software or update
# existing softwares pretty much every week. The update cannot be deployed on
# every server at the same time, because the server may have to be taken down
# for the install. Also, the update should not be done one at a time, because
# it will take a lot of time. There are sets of servers that cannot be taken
# down together, because they have certain critical functions. This is a
# typical scheduling application of graph coloring problem. It turned out that
# 8 colors were good enough to color the graph of 75000 nodes. So they could
# install updates in 8 passes.

def graph_greedy_coloring(graph):
    result = {}
    for v in graph:
        result[v] = -1

    available = [False for _ in range(len(graph))]
    for color in range(len(graph)):
        available[color] = False

        for u in range(1, len(graph)):

