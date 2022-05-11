"""

for brute force we can do backtracking and go through all the combinations. the time complexity factorial of n

we can put this as part of the heap and add things to the max heap.
we reset the heap to empty once there is a travel happening.
this is a greedy way of doing

greedy time complexity: O(nlogn) since the max value of the heap will be n

"""

from heapq import heappush, heappop

def min_refueling(target, startfuel, stations):
    if len(stations)==0:
        if startfuel >= target:
            return 0
        else:
            return -1

    stations.sort()
    stations = [[0,0]] + stations
    heap = []
    curr = 0
    j = 0
    while startfuel >= 0 and startfuel < target - stations[curr][0]:
        # first get the max position that the car can travel to
        i = curr + 1
        while i < len(stations) and startfuel >= stations[i][0] - stations[curr][0]:
            heappush(heap, [-stations[i][1], stations[i], i])
            i += 1
        print(f'{heap=}')

        # now get the biggest petrol
        if heap:
            biggest_petrol = heap[0]
            distance = biggest_petrol[1][0] - stations[curr][0]
            gain = biggest_petrol[1][1]
            startfuel = startfuel - distance + gain
            j += 1
            heap = []
            curr = biggest_petrol[2]
        else:
            break
        print(f'{distance=}, {startfuel=}')

    if startfuel >= target - stations[curr][0]:
        return j
    else:
        return -1


# the answers are wrong
target = 1000
startFuel = 299
stations = [[13,21],[26,115],[100,47],[225,99],[299,141],[444,198],[608,190],[636,157],[647,255],[841,123]]
print(min_refueling(target, startFuel, stations))

# target = 100
# startFuel = 50
# stations = [[25,50],[50,25]]
# print(min_refueling(target, startFuel, stations))

# target = 1
# startFuel = 1
# stations = []
# print(min_refueling(target, startFuel, stations))

# target = 100
# startFuel = 1
# stations = [[10,100]]
# print(min_refueling(target, startFuel, stations))

# target = 100
# startFuel = 10
# stations = [[10,60],[20,30],[30,30],[60,40]]
# print(min_refueling(target, startFuel, stations))

# target = 100
# startFuel = 25
# stations = [[25,25],[50,25],[75,25]]
# print(min_refueling(target, startFuel, stations))




# =========================
# this strategy does not work