"""

username1: cat dog
username2: elephant fox tiger duck
username1: giraffe


hi this is joydeep

logfile

list username, message type

find the k most talkative users

number of words each user types

param k is also given

edge cases:
  the file empty?

messages are sep by any whitespace

size of the input is m
no. of users is n

algo:
	init a hashmap of the {users: count}
	read the file line by line and then update the count corr to the users
    once the full file is read then create a heap of the the counts with the users
    then get the first k elements from the heap

going through the file
time complex: O(n *  characters in the line)
space complex: O(n)

getting the top k:
time complexity: O(klogn)
space complexity: O(n)

"""


from heapq import heapify, heappush, heappop
from collections import defaultdict
class FileReader:
  """
  A file reader to implement some file methods

  Args:
  	filename (str): path to the filename
  """
  def __init__(self, filename):
    self.filename = filename

  def get_username_words(self, line):
    i = 0
    for i, ch in enumerate(line):
      if ch == ":":
        if i+1 < len(line):
          return line[:i], line[i+1:]
        else:
          return line[:i], ""

  def get_usercounts(self):
    """
    Get the word counts from the file for the users

    going through the file
	time complex: O(n *  characters in the line)
	space complex: O(n)

    Returns
    	dict: username -> counts
    """
    word_counts = defaultdict(int) # {}
    with open(self.filename) as f:
      for line in f:
        if line:
          username, words = self.get_username_words(line) # username1, cat dog
          num_words = len(words.split()) # 1
          word_counts[username] += num_words # {u1: 3, u2: 4, }
    return word_counts

  def k_most_talkative(self):
    """
    get k most talkative users

    getting the top k:
	time complexity: O(n + klogn)
	space complexity: O(n)

    Yields:
	    username (str)
    """
    word_counts = self.get_usercounts()  # {u1: 3, u2: 4, }
    word_counts_heap = [(-count, username) for username, count in word_counts.items()] # [(-4, username), (-3, username)]
    heapify(word_counts_heap) # [(-4, u2), (-3, u1)]
    counter = 0
    while word_counts_heap or counter < k:
      _, username = heappop(word_counts_heap)
      counter += 1 # 1, 2
      yield username # u2, u1

"""

username1: cat dog
username2: elephant fox tiger duck
username1: giraffe

username1: cat dog
username2: elephant fox tiger
username1: giraffe

"""

























