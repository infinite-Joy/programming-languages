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

def add(occ, ele, solution):
  if occ<=-2:
    solution += "{}{}".format(ele, ele)
    occ += 2
  elif occ==-1:
    solution += "{}".format(ele)
    occ += 1
  return occ, solution

def longest_happy_string(abc):
  print(abc)
  i = 0
  queue = []
  for k, v in abc.items():
    q.heappush(queue, (-v, i, k))
    i += 1
  print(queue)
  solution = ""
  while len(queue)>0:
    import time; time.sleep(1)
    print(queue, solution)
    #__import__('pdb').set_trace()
    occu1, i, elem1 = q.heappop(queue)
    occu1, solution = add(occu1, elem1, solution)

    if len(queue)==0 and occu1<0:
      return solution

    occu2, j, elem2 = q.heappop(queue)
    occu2, solution = add(occu2, elem2, solution)

    if occu2 < 0:
      q.heappush(queue, (occu2, j, elem2))
    if occu1 < 0:
      q.heappush(queue, (occu1, i, elem1))

  return solution

print(longest_happy_string(dict(a=1, b=1, c=7)))
print("*"*20)
print(longest_happy_string(dict(a = 2, b = 2, c = 1)))
print("*"*20)
print(longest_happy_string(dict(a = 7, b = 1, c = 0)))
