#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the checkMagazine function below.
# this can be done using hashmap.
# will create hash map out of the note
# and will be decrementing the count. if it reaches 0 then remove the elem.
# if all elements removed we can return yes
# if the end of the magazine reached then will be returning no
# time complexity O(n+m)
# space complexity: O(len(note))
def checkMagazine(magazine, note):
    magazine = magazine.split()
    note = note.split()

    vocab = {}
    for w in note:
        if w not in vocab:
            vocab[w] = 0
        vocab[w] += 1

    for w in magazine:
        if w in vocab:
            vocab[w] -= 1
            if vocab[w] == 0:
                del vocab[w]
        if len(vocab) == 0:
            return True

    return False

print(checkMagazine("give me one grand today night", "give one grand today"))

