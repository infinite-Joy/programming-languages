from astar import Node, pathFind


def test_Node_init():
    node = Node(1, 2, 3, 4)
    assert node.x_position == 1
    assert node.y_position == 2
    assert node.distance == 3
    assert node.priority == 4


def test_comparison_method():
    node = Node(1, 2, 3, 4)
    node1 = Node(1, 2, 3, 5)
    assert node < node1
    node2 = Node(1, 2, 3, 3)
    assert node > node2


def test_node_estimate():
    node = Node(1, 2, 3, 4)
    dnode = node.estimate(4, 6)
    assert dnode == 5


def test_node_updatePriority():
    node = Node(1, 2, 3, 4)
    node.updatePriority(4, 6)
    assert node.priority == 53


def test_node_nextMove():
    node = Node(1, 2, 3, 4)
    node.nextMove(8, 1)
    assert node.distance == 17
    node.nextMove(8, 2)
    assert node.distance == 27
    node.nextMove(7, 1)
    assert node.distance == 37

def test_pathFind():
    the_map = [[0, 0], [0, 0]]
    possible_directions = 3
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    res = pathFind(the_map, 30, 30, possible_directions,dx, dy, xA, yA, xB, yB )
    assert res == 1
