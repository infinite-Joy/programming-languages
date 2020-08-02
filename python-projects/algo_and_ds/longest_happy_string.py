"""
the priority queue makes most sense in this case

so i can bring in the largest element and bring in two elements.

and bring in 2 elements

and then we can take the second largest and take 2

for each operation we will be doing logn operations

hence time complexity is O(nlgn)
space complexity is O(n)

============================
"""

import heapq as q

def add(occ, ele, builder):
  if occ<=-2:
    builder += "{}{}".format(ele, ele)
    occ += 2
  elif occ==-1:
    builder += "{}".format(ele)
    occ += 1
  return occ, builder

def longest_happy_string(abc):
  print(abc)
  i = 0
  queue = []
  for k, v in abc.items():
    if v > 0:
      q.heappush(queue, (-v, i, k))
    i += 1
  print(queue)
  builder = ""
  while len(queue)>1:
    import time; time.sleep(1)
    print(queue, builder)
    #__import__('pdb').set_trace()
    #first time
    occu1, i, elem1 = q.heappop(queue)
    occu1, builder = add(occu1, elem1, builder)

    # second time
    occu2, j, elem2 = q.heappop(queue)
    occu2, builder = add(occu2, elem2, builder)

    if occu1 < 0:
      q.heappush(queue, (occu1, i, elem1))
    if occu2 < 0:
      q.heappush(queue, (occu2, j, elem2))

  if len(queue) > 0:
    if builder[-1] == queue[0][2] and builder[-1] != builder[-2]:
      builder += queue[0]
    elif builder[-1] != queue[0][2]:
      if queue[0][0] <= -2:
        builder = builder + queue[0][2] + queue[0][2]
      else:
        builder = builder + queue[0][2]

  return builder

print(longest_happy_string(dict(a=1, b=1, c=7)))
print("*"*20)
print(longest_happy_string(dict(a = 2, b = 2, c = 1)))
print("*"*20)
print(longest_happy_string(dict(a = 7, b = 1, c = 0)))
