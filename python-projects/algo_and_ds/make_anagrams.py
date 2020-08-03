#!/bin/python3

import math
import os
import random
import re
import sys



from collections import defaultdict

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    # this can be done using a hash map of the chars
    # for the first run do addition
    # for the second string do the deletion
    # this can be done by either using a hashmap
    # or by sorting the strings and then using 2 pointer
    print(a)
    print(b)

    anag = {}
    for ch in a:
        if ch not in anag:
            anag[ch] = 0
        anag[ch] += 1
    print(anag)

    uniq = 0
    for ch in b:
        print(ch, uniq)
        if ch in anag:
            print(ch, 'is present in anag')
            anag[ch] -= 1
            print('anag[{}] = {}'.format(ch, anag[ch]))
            if anag[ch] == 0:
                del anag[ch]
        else:
            uniq += 1

    print(anag)
    return sum(anag.values()) + uniq


print(makeAnagram('fcrxzwscanmligyxyvym', 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'))
