HORIZONTAL_MAP_SIZE = 60
VERTICAL_MAP_SIZE = 60

map = []
open_nodes_map = []
dir_map = []
possible_directions = 8

dx[possible_directions] = [1, 1, 0, -1, -1, -1, 0, 1]
dy[possible_directions] = [0, 1, 1, 1, 0, -1, -1, -1]

class Node:

    def __init__(self, xPos, yPos, level, priority):
        self.xPos = xPos
        self.yPos = yPos
        self.level = level
        self.priority = priority

    def updatePriority(self, xDest, yDest):
        self.priority = self.level + self.estimate(xDest, yDest)*10; #A*

    def nextLevel(self, directions, d):
        if directions == 8 and d % 2 is not 0:
            self.level += 14
        else:
            self.distance += 10

    def estimate(self, xDest, yDest):
        xd = yd = d = 0
        xd = xDest - self.xPos
        yd = yDest - self.yPos

        #Euclidean Distance
                              d=static_cast<int>(sqrt(xd*xd+yd*yd));
