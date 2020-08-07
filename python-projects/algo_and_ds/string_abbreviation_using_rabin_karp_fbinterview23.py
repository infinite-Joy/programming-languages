#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/test/61sq9qfa63d/questions/4hmpnticng5



# Complete the abbreviation function below.
# this is similar to finding the substring in a string
# if found check if there are uppercase words in the reminaing string
# if there are then we will continue.
# if we reached the end of the string then we say that we have not
# recieved anything similar and then we will exit saying NO
# complexity is O(n+m)

from collections import deque

def checking(queue: 'deque', substring: str) -> bool:
    mainstr = "".join(queue)
    return mainstr == substring

def rabin_karp(substr: str, mainstr: str) -> int:
    """Check if substring in main string using rabin karp"""
    base = 26
    mainstrhash = 0
    substrhash = 0
    subsize = len(substr)
    queue = deque([])
    for i, ch in enumerate(mainstr):
        print(i, ch, queue)
        ch = ch.lower()
        if i < len(substr):
            queue.append(ch)
            mainstrhash = mainstrhash * base + ord(ch)
            substrhash = substrhash * base + ord(substr[i].lower())
            if i == len(substr)-1 and mainstrhash == substrhash and checking(queue, substr.lower()) is True:
                yield i-subsize+1, i+1
        else:
            biggest = queue.popleft()
            mainstrhash -= ord(biggest) * (base**(subsize-1))
            mainstrhash = mainstrhash * base + ord(ch)
            print(mainstrhash, substrhash)
            queue.append(ch)
            #if mainstrhash ==68219:
            #    __import__('pdb').set_trace()
            if mainstrhash == substrhash and checking(queue, substr.lower()) is True:
                yield i-subsize+1, i+1

def abbreviation(a, b):
    mainstr = a
    substr = b
    print(substr, mainstr)
    matches = False
    for start, end in rabin_karp(substr, mainstr):
        print('checking if remaining are upper',start, end)
        matches = True
        if any([x.isupper() for x in mainstr[:start]]):
            return False
        if any([x.isupper() for x in mainstr[end:]]):
            return False
    return matches

#print(abbreviation('daBcd', "ABC"))
#print(abbreviation('Pi', "P"))
print(abbreviation('Kqiwysuaqm', "K"))



