"""

Given a function KNOWS(A,B), which returns 1 if A knows B (and not necessarily the other way around) and 0 if A does not know B.

A Celebrity is one who does not know anyone,
and one who is known by everybody.

For a list of N people, find all celebrities in linear time.

basically what i can do is that make an indegree hashmap

and then do a dfs and then update the indegree whenever we get something

finally whenever we get something that indegree

"""

# https://leetcode.com/problems/find-the-celebrity/

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

from functools import reduce
class Solution:
    def findCelebrity(self, n: int) -> int:
        if n <= 1: return n
        candidate = 0
        # find the candidate
        for i in range(n):
            if knows(candidate, i):
                candidate = i
        # verify
        for i in range(n):
            if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
                return -1
        return candidate


this is the better solution using 2 pass. the graph based solution does not work and takes in more memory

