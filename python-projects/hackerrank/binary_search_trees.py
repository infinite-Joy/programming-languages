from collections import namedtuple

def binary_search(key, arr, left, right):
    if right < left:
        return -1
    else:
        mid = (right - left) // 2
        mid = mid + left
        if key < arr[mid]:
            right = mid
            return binary_search(key, arr, left, right)
        elif key > arr[mid]:
            left = mid
            return binary_search(key, arr, left, right)
        else:
            return mid


def search(key, arr):
    left, right = 0, len(arr)-1
    return binary_search(key, arr, left, right)


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
print(search(67, primes))
print(primes.index(67))


# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem


class BinaryTree:

    class _node:
        def __init__(self, value, parent=None, left=None, right=None, count=1):
            self.value = value
            self.parent = parent
            self.left = left
            self.right = right
            self.count = count

        def _get_value(self, v):
            if v is None:
                return None
            else:
                return v.value

        def __repr__(self):
            return "Node: value: {}, parent: {}, left: {}, right: {}, count: {}".format(
                self.value, self._get_value(self.parent), self._get_value(self.left), self._get_value(self.right), self.count)

    def __init__(self, r):
        self.r = self._node(r)

    def insert(self, e, p=None):
        if p is None:
            p = self.r

        if p.value < e:
            if p.left:
                self.insert(e, p.left)
            else:
                e = self._node(e, p)
                print("parent of {} is {}".format(e.value, e.parent.value))
                p.left = e
        elif p.value > e:
            if p.right:
                self.insert(e, p.right)
            else:
                e = self._node(e, p)
                p.right = e
        else:
            p.count += 1

    def _validate(self, e):
        for node in self._print_tree_inorder(self.r):
            if node.value == e:
                return node
        raise ValueError("No element found for {}".format(e))

    def get_children(self, node):
        return len(list(filter(None, [node.left, node.right])))

    def _remove_connection_with_parent(self, node, parent):
        if parent is None:
            return
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
        node.parent = None
        return parent

    def find_minimum(self, sub_tree=None):
        if sub_tree is None:
            sub_tree = self.r
        if sub_tree.left:
            return self.find_minimum(sub_tree.left)
        return sub_tree

    def delete(self, e):
        if isinstance(e, self._node):
            node = e
        else:
            node = self._validate(e)
        number_of_children = self.get_children(node)
        parent_node = node.parent
        if number_of_children == 0:
            self._remove_connection_with_parent(node, parent_node)
        if number_of_children == 1:
            if node.left:
                # get parent and child
                left_node = node.left

                # disenfranchise this node
                if parent_node is not None:
                    parent_node.left = left_node
                left_node.parent = parent_node
            if node.right:
                # get the values
                right_node = node.right

                # disenfranchise this node
                if parent_node is not None:
                    parent_node.right = right_node
                right_node.parent = parent_node
        if number_of_children == 2:
            # find the minimum in the right node
            inorder_successor = self.find_minimum(node.right)
            self.delete(inorder_successor)

            left_node = node.left
            right_node = node.right
            if parent_node is not None:
                parent_node.right = inorder_successor
            inorder_successor.left = left_node
            inorder_successor.right = right_node

            # remove node connections
            node.left = None
            node.right = None

        node.parent = node # convention for deprecated node


    def _print_tree_inorder(self, p=None):
        if p.left:
            for left_node in self._print_tree_inorder(p.left):
                yield left_node
        yield p
        if p.right:
            for right_node in self._print_tree_inorder(p.right):
                yield right_node

    def print_tree_inorder(self):
        for node in self._print_tree_inorder(self.r):
            print(node.value, end=" ")
        print()

    def find_place_in_ranking(self, element):
        ranking = 1
        for node in self._print_tree_inorder(self.r):
            if node.value == element:
                return ranking
            ranking += 1


b = BinaryTree(5)
b.insert(4)
b.insert(6)
b.print_tree_inorder()

scores = [100, 100, 50, 40, 40, 20, 10]
#scores = [100, 100, 50]

from random import shuffle
shuffle(scores)
scores = [50, 100, 100, 20, 40, 40, 10]
print("shiffled scores", scores)

b = BinaryTree(scores[0])
for s in scores[1:]:
    b.insert(s)

b.print_tree_inorder()

b.insert(5)
#print(b.find_place_in_ranking(5))
#
#
print("for checking delete with one node")
print("deleting 20")
print("before deletion", b.print_tree_inorder())
b.delete(20)
print("after deletion", b.print_tree_inorder())



print("before deletion", b.print_tree_inorder())
b.delete(50)
print("after deletion", b.print_tree_inorder())

print(b.find_minimum().value)

print("for checking delete with 2 nodes")
#scores = [100, 100, 50, 40, 40, 20, 10]
scores = [40, 40, 100, 100, 50, 60, 70, 20, 10]

#from random import shuffle
#shuffle(scores)
print("shiffled scores", scores)
b = BinaryTree(scores[0])
for s in scores[1:]:
    b.insert(s)

b.print_tree_inorder()

b.insert(5)
print("before deletion")
b.print_tree_inorder()
b.delete(50)
print("after deletion")
b.print_tree_inorder()
