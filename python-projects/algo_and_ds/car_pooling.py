"""
a simple way is to map all the stations and then go through the trips and map the capacity for the different stations
if the capacity goes beyond a number then you mark this as false.

time O(n*m)
space O(max-min)


    Save all time points and the change on current capacity
    Sort all the changes on the key of time points.
    Track the current capacity and return false if negative


"""

def carpooling(trips, capacity):
    start, end = min(f for _, f, _ in trips), max(t for _, _, t in trips)
    stations = [0] * (end - start + 1)
    for n, f, t in trips:
        stations[f - start] += n
        stations[t - start] -= n
    print(stations)
    if stations[0] > capacity:
        return False
    for curr in range(1, len(stations)):
        stations[curr] = stations[curr-1] + stations[curr]
        if stations[curr] > capacity:
            return False
    print(stations)
    return True

# trips = [[2,1,5],[3,5,7]]
# capacity = 3
# print(carpooling(trips, capacity))

trips = [[9,0,1],[3,3,7]]
capacity = 4
print(carpooling(trips, capacity))

# ==============

"""
a simple way is to map all the stations and then go through the trips and map the capacity for the different stations
if the capacity goes beyond a number then you mark this as false.

time O(n*m)
space O(max-min)

"""

from heapq import heapify, heappop


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        start, end = min(f for _, f, _ in trips), max(t for _, _, t in trips)
        stations = [0] * (end - start + 1)
        for n, f, t in trips:
            stations[f - start] += n
            stations[t - start] -= n
        # print(stations)
        if stations[0] > capacity:
            return False
        for curr in range(1, len(stations)):
            stations[curr] = stations[curr-1] + stations[curr]
            if stations[curr] > capacity:
                return False
        # print(stations)
        return True