"""
Imagine you are playing a board game. You roll a 6-faced dice and move forward the same number of spaces that you rolled. If the finishing 
point is “n” spaces away from the starting point, please implement a program that calculates how many possible ways there are to arrive 
exactly at the finishing point.
"""

from itertools import islice, cycle
from sys import argv

try:
    range = xrange
except NameError:
    pass

def fiblike(tail):
    for x in tail:
            yield x
    for i in cycle(range(len(tail))):
            tail[i] = x = sum(tail)
            yield x

for arg in argv[1:]:
    number = int(arg)
    fib = fiblike([1] + [2 ** i for i in range(5)])
    items = list(islice(fib, number))
    print(items[-1])

