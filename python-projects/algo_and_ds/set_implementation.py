import random
from itertools import cycle

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1024
        self.no_elems = 0
        self.elems = [None] * self.size

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        idx = hash(val) & (self.size-1)
        if self.elems[idx] is None:
            self.elems[idx] = val
            self.no_elems += 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        idx = hash(val) & (self.size-1)
        if self.elems[idx] is None:
            return False
        else:
            self.no_elems -= 1
            self.elems[idx] = None

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        choice = random.choice(range(self.size))
        while True:
            for i in cycle(range(self.size)):
                idx = choice + i
                if idx >= self.size:
                    idx = idx - self.size
                if self.elems[idx] is not None:
                    return self.elems[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
