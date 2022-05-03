"""
implementing this using rabin karp


"""

import string

word_map[ch] = {ch: val for val, ch in enumerate(list(string.ascii_lowercase))}

def get_word_hash(word):
    hashval = 0
    for ch in word:
        hashval = hashval*len(wordmap) + word_map[ch]
    return hashval

def get_rolling_hash(word, hashval, incoming, outgoing=None):
    if outgoing:
        hashval = hashval % (word[outgoing] * (len(wordmap) ** (len(word) - 1)))
    hashval = hashval * len(wordmap)
    return rollinghash

def find_substring(s, words):
    # preprocessing for the patterns
    phashes = {}
    total_hash = 0
    for word in words:
        curr_hash = get_word_hash(word)
        total_hash += curr_hash
        phashes[curr_hash] = word

    total = len(words) * len(words[0])

    i = 0
    j = 0
    for j in range(total):
        


    for i in range(len(s)-total+1):
        j = i + total


