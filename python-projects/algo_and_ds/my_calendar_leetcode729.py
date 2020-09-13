"""
my calendar
we can create interval trees out of it and then
search it in the interval tree.
make an interval tree out of the two
time complexity should be O(height of the tree) which is log number of values if balanced else number of intervals if unbalanced
========================
class Node:
    def __init__(self, interval):
        self.interval = interval
        self.left = None
        self.right = None
class IntervalTree:
    def __init__(self):
        self.root = None
    def add_node(self, interval):
        if self.root is None:
            self.root = Node(interval)
            return True
        else:
            node = self.root
            prev = None
            leftlimit = None
            rightlimit = None
            while node:
                prev = node
                if interval[0] == node.interval[0]:
                    return False
                elif  interval[0] < node.interval[0]:
                    rightlimit = node
                    node = node.left
                else:
                    leftlimit = Node
                    node = node.right
            if leftlimit[1] > interval[0]:
                return False
            elif rightlimit[0] < interval[1]:
                return False
            else:
                if prev == leftlimit:
                    prev.right = Node(interval)
                else:
                    prev.left = Node(interval)
        return True
class MyCalendar:
def __init__(self):
    self.tree = IntervalTree()
def book(self, start: int, end: int) -> bool:
    return self.add_node([start, end])



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

"""

class Node:
    def __init__(self, interval):
        self.interval = interval
        self.left = None
        self.right = None
class IntervalTree:
    def __init__(self):
        self.root = None
    def add_node(self, interval):
        if self.root is None:
            self.root = Node(interval)
        else:
            node = self.root
            prev = None
            leftlimit = None
            rightlimit = None
            while node:
                print(node)
                prev = node
                if interval[0] == node.interval[0]:
                    return False
                elif interval[0] < node.interval[0]:
                    rightlimit = node
                    node = node.left
                else:
                    leftlimit = node
                    node = node.right
            print(leftlimit, rightlimit)
            if leftlimit and leftlimit.interval[1] > interval[0]:
                return False
            elif rightlimit and rightlimit.interval[0] < interval[1]:
                return False
            else:
                if interval[0] < prev.interval[0]:
                    prev.left = Node(interval)
                else:
                    prev.right = Node(interval)
        return True
class MyCalendar:

    def __init__(self):
        self.intervaltree = IntervalTree()

    def book(self, start: int, end: int) -> bool:
        return self.intervaltree.add_node([start, end])

# test cases
cal = MyCalendar();
obj = MyCalendar()
print(obj.book(10, 20));
print(obj.book(15, 25));
print(obj.book(20, 30));
