"""

0, 15
mid 7 next bat val = currbattery - (prevlevel - current level)
keep checking if my battery is not 0 or my prevlevel - next level is negative

time complexity: O(n log(max(n)))

route = [ [0, 2, -11], # 4
          [0,   2, -10], battery: 5
          [3,   5,  -1], b: 15
          [9,  20,  -6], b: 9
          [10, 12, -15], b: 0
          [10, 10,  -8] ]b: 7


start =
end =  [10, 10,  8]


"""

def calc_drone_min_energy(route):
  maxval = -float('inf')
  for _, _, val in route:
    maxval = max(maxval, val)

  return maxval - route[0][2]

print(calc_drone_min_energy([ [0,   2, 10],
                  [3,   5,  0],
                  [9,  20,  6],
                  [10, 12, 15],
                  [10, 10,  8] ]))
