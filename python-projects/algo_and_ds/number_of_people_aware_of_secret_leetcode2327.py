"""
This seems like a dp solution

this seems to be like a BFS solution

"""

from collections import deque
from itertools import count


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        
        counter = count(start=1, step=1)
        
        def bfs(n):
            if n == 0 or n == 1:
                return n
            else:
                queue = deque([(next(counter), 1, 1)])
                while queue:
                    node, level, start = queue.popleft()
                    if level > n:
                        return len(queue)
                    
                    if level < start+delay:
                        queue.append((node, level+1, start))
                    elif start + delay <= level <= start+forget:
                        queue.append((node, level+1, start))
                        queue.append((next(counter), level+1, level+1))
                    else:
                        # this will do nothing hence forget
                        pass
                        
        return bfs(n)

from collections import deque
from itertools import count

def peopleAwareOfSecret(n: int, delay: int, forget: int) -> int:
        
    counter = count(start=1, step=1)
    
    def bfs(n):
        level_count = 0
        if n == 0 or n == 1:
            return n
        else:
            queue = deque([(next(counter), 1, 1)])
            while queue:
                # print(queue)
                node, level, start = queue.popleft()
                if level == n:
                    level_count += 1
                if level > n:
                    return level_count
                
                if level < start+delay-1:
                    queue.append((node, level+1, start))
                elif start + delay - 1 <= level < start+ forget - 1:
                    queue.append((node, level+1, start))
                    queue.append((next(counter), level+1, level+1))
                else:
                    # this will do nothing hence forget
                    pass
                    
    return bfs(n)

print(peopleAwareOfSecret(6, 2, 4), 5)
print(peopleAwareOfSecret(4, 1, 3), 6)
print(peopleAwareOfSecret(425, 81, 118), 6)