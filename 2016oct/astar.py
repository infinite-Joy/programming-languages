"""
# A* Shortest Path Algorithm
# http://en.wikipedia.org/wiki/A*
"""
from __future__ import print_function
from heapq import heappush, heappop # for priority queue
import math
import time
import random

# for compatibility with both py2 and py3
try:
    input = raw_input
except NameError:
    pass

class Node:

    def __init__(self, x_position, y_position, distance, priority):
        self.x_position = x_position
        self.y_position = y_position
        self.distance = distance
        self.priority = priority

    def __lt__(self, other):
        """
        comparison method for priority queue
        """
        return self.priority < other.priority

    def updatePriority(self, xDest, yDest):
        """
        employs the a-star heuristic
        """
        self.priority = self.distance + self.estimate(xDest, yDest) * 10

    def nextMove(self, possible_directions, d):
        """
        give higher priority to going straight instead of diagonally
        d: direction to move
        """
        if possible_directions == 8 and d % 2 != 0:
            self.distance += 14
        else:
            self.distance += 10

    def estimate(self, xDest, yDest):
        """
        Estimation function for the remaining distance to the goal.
        """
        dx = xDest - self.x_position
        dy = yDest - self.y_position
        # Euclidian Distance
        d = math.sqrt(dx ** 2 + dy ** 2)
        # Manhattan distance: d = abs(xd) + abs(yd)
        # Chebyshev distance: d = max(abs(xd), abs(yd))
        return d


def pathFind(the_map, horizontal_size_of_map, vertical_size_of_map, possible_directions, dx, dy, xA, yA, xB, yB):
    """
    A-star algorithm. The path returned will be a string of digits of direction
    """
    closed_nodes_map = []  # map of closed (tried-out) nodes
    open_nodes_map = []  # map of open (not-yet-tried) nodes
    dir_map = []  # map of possible_directions
    row = [0] * horizontal_size_of_map

    for i in range(vertical_size_of_map):  # create 2d arrays
        closed_nodes_map.append(list(row))
        open_nodes_map.append(list(row))
        dir_map.append(list(row))

    pq = [[], []]  # priority queues of open (not-yet-tried) nodes
    pqi = 0  # priority queue index
    # create the start node and push into list of open nodes
    n0 = Node(xA, yA, 0, 0)
    n0.updatePriority(xB, yB)
    heappush(pq[pqi], n0)
    open_nodes_map[yA][xA] = n0.priority  # mark it on the open nodes map
    # A* search
    while len(pq[pqi]) > 0:
        # get the current node w/ the highest priority from the list of open nodes
        n1 = pq[pqi][0]  # top node
        n0 = Node(n1.x_position, n1.y_position, n1.distance, n1.priority)
        x = n0.x_position
        y = n0.y_position
        heappop(pq[pqi])  # remove the node from the open list
        open_nodes_map[y][x] = 0
        closed_nodes_map[y][x] = 1  # mark it on the closed nodes map
        # quit searching when the goal is reached if n0.estimate(xB, yB) == 0:
        if x == xB and y == yB:
            # generate the path from finish to start by following the possible_directions
            path = ''
            while not (x == xA and y == yA):
                j = dir_map[y][x]
                c = str((j + possible_directions // 2) % possible_directions)
                path = c + path
                x += dx[j]
                y += dy[j]
            return path
        # generate moves (child nodes) in all possible possible_directions
        for i in range(possible_directions):
            xdx = x + dx[i]
            ydy = y + dy[i]
            if not (xdx < 0 or xdx > horizontal_size_of_map - 1 or ydy < 0 or ydy > vertical_size_of_map - 1
                    or the_map[ydy][xdx] == 1 or
                    closed_nodes_map[ydy][xdx] == 1):
                # generate a child node
                m0 = Node(xdx, ydy, n0.distance, n0.priority)
                m0.nextMove(possible_directions, i)
                m0.updatePriority(xB, yB)
                # if it is not in the open list then add into that
                if open_nodes_map[ydy][xdx] == 0:
                    open_nodes_map[ydy][xdx] = m0.priority
                    heappush(pq[pqi], m0)
                    # mark its parent node direction
                    dir_map[ydy][xdx] = (i + possible_directions // 2) % possible_directions
                elif open_nodes_map[ydy][xdx] > m0.priority:
                    # update the priority
                    open_nodes_map[ydy][xdx] = m0.priority
                    # update the parent direction
                    dir_map[ydy][xdx] = (i + possible_directions // 2) % possible_directions
                    # replace the node by emptying one pq to the other one
                    # except the node to be replaced will be ignored and
                    # the new node will be pushed in instead
                    while not (pq[pqi][0].x_position == xdx and
                               pq[pqi][0].y_position == ydy):
                        heappush(pq[1 - pqi], pq[pqi][0])
                        heappop(pq[pqi])
                    heappop(pq[pqi]) # remove the target node
                    # empty the larger size priority queue
                    # to the smaller one
                    if len(pq[pqi]) > len(pq[1 - pqi]):
                        pqi = 1 - pqi
                    while len(pq[pqi]) > 0:
                        heappush(pq[1-pqi], pq[pqi][0])
                        heappop(pq[pqi])
                    pqi = 1 - pqi
                    heappush(pq[pqi], m0) # add the better node instead
    return '' # if no route found


if __name__ == "__main__":
    possible_directions = 8 # number of possible directions to move on the map
    if possible_directions == 4:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
    elif possible_directions == 8:
        dx = [1, 1, 0, -1, -1, -1, 0, 1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]

    horizontal_size_of_map = 30
    vertical_size_of_map = 30
    the_map = []
    row = [0] * horizontal_size_of_map
    for i in range(vertical_size_of_map): # create empty map
        the_map.append(list(row))

    # fillout the map with a '+' pattern
    for x in range(horizontal_size_of_map // 8, horizontal_size_of_map * 7 // 8):
        the_map[vertical_size_of_map // 2][x] = 1
    for y in range(vertical_size_of_map//8, vertical_size_of_map * 7 // 8):
        the_map[y][horizontal_size_of_map // 2] = 1

    # randomly select start and finish locations from a list
    sf = []
    sf.append((0, 0, horizontal_size_of_map - 1, vertical_size_of_map - 1))
    sf.append((0, vertical_size_of_map - 1, horizontal_size_of_map - 1, 0))
    sf.append((horizontal_size_of_map // 2 - 1, vertical_size_of_map // 2 - 1, horizontal_size_of_map // 2 + 1, vertical_size_of_map // 2 + 1))
    sf.append((horizontal_size_of_map // 2 - 1, vertical_size_of_map // 2 + 1, horizontal_size_of_map // 2 + 1, vertical_size_of_map // 2 - 1))
    sf.append((horizontal_size_of_map // 2 - 1, 0, horizontal_size_of_map // 2 + 1, vertical_size_of_map - 1))
    sf.append((horizontal_size_of_map // 2 + 1, vertical_size_of_map - 1, horizontal_size_of_map // 2 - 1, 0))
    sf.append((0, vertical_size_of_map // 2 - 1, horizontal_size_of_map - 1, vertical_size_of_map // 2 + 1))
    sf.append((horizontal_size_of_map - 1, vertical_size_of_map // 2 + 1, 0, vertical_size_of_map // 2 - 1))
    (xA, yA, xB, yB) = random.choice(sf)

    print('Map size (X,Y): ', horizontal_size_of_map, vertical_size_of_map)
    print('Start: ', xA, yA)
    print('Finish: ', xB, yB)
    t = time.time()
    route = pathFind(the_map, horizontal_size_of_map, vertical_size_of_map, possible_directions, dx, dy, xA, yA, xB, yB)
    print('Time to generate the route (seconds): ', time.time() - t)
    print('Route:')
    print(route)

    # mark the route on the map
    if len(route) > 0:
        x = xA
        y = yA
        the_map[y][x] = 2
        for i in range(len(route)):
            j = int(route[i])
            x += dx[j]
            y += dy[j]
            the_map[y][x] = 3
        the_map[y][x] = 4

    # display the map with the route added
    print('Map:')
    for y in range(vertical_size_of_map):
        for x in range(horizontal_size_of_map):
            xy = the_map[y][x]
            if xy == 0:
                print('.' ,end="") # space
            elif xy == 1:
                print('O' ,end="") # obstacle
            elif xy == 2:
                print('S', end="") # start
            elif xy == 3:
                print('R', end="") # route
            elif xy == 4:
                print('F', end="") # finish
        print()
