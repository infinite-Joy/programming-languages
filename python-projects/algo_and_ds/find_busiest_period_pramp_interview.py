"""
ok
can you see the algo?

yes i can

data = [ [1487799425, 14, 1],
         [1487799425, 4,  0],
         [1487799425, 2,  0],
         [1487800378, 10, 1],
         [1487801478, 18, 0],
         [1487801478, 18, 1],
         [1487901013, 1,  0],
         [1487901211, 7,  1],
         [1487901211, 7,  0] ]

first approach:

algorithm:
    add or subtract based on the 1 or 0
    keep updating the max
    return the max

time complexity: O(size of the arr)
space complexity: O(1)

does this make sense for now?

i am thinking this would work, but maybe i can implement a bst here
ok

second approach: thinking about bst
  so basically for i am thinking about what is the parameter that i should search for

i think ur first approach is good

ok. shall i start coding for that?

i am going ahead and codingfor that then

yeah ok , do it

i think the code is done. will go ahead and check if i am not missing out on anything

i think it is good. i am going ahead and testing it on the test case

this did not work correctly;. looking at the reason

excuse me joel , i need to end the session as iam not feel

ing we

no problemll im really sorry

no problem. thanks for your time
"""

def find_busiest_period(data):
  maxpeople = 0
  max_people_timestamp = 0
  people_in_mall = 0
  for timestamp, number, enter_exit_flag in data:
    if enter_exit_flag == 0:
      adder = -1
    else:
      adder = 1
    people_in_mall += adder * number
    maxpeople = max(maxpeople, people_in_mall)
    if maxpeople == people_in_mall:
      max_people_timestamp = timestamp
  return max_people_timestamp


data = [ [1487799425, 14, 1],
           [1487799425, 4,  0],
           [1487799425, 2,  0],
           [1487800378, 10, 1],
           [1487801478, 18, 0],
           [1487801478, 18, 1],
           [1487901013, 1,  0],
           [1487901211, 7,  1],
           [1487901211, 7,  0] ]

print(find_busiest_period(data))
