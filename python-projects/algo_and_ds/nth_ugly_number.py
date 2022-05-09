
from heapq import heapreplace, heapify

def main(n):
    if n == 1: return 1
        
    mul = [1,1,1]
    factor = [2,3,5]
    for _ in range(n):
        candidates = [m*f for m, f in zip(mul, factor)]
        minval = min(candidates)
        minidx = 0
        for i, el in enumerate(candidates):
            if minval == el:
                mul[i] += 1
        print(min(candidates))
    return minval

# print(main(10))
# print(main(13))
print(main(11))