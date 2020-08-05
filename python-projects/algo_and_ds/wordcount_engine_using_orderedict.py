from collections import OrderedDict
from typing import List, Tuple
from itertools import accumulate

def counter(freqs, maxval):
    counts = [0] * (-1*maxval)
    print(freqs)
    print(counts)
    for s, f in freqs:
        print(s,f)
        counts[f] += 1
    return counts


def build_solution(freqs, counts):
    sol = [[] for _ in range(len(freqs))]
    for string, freq in freqs[::-1]:
        counts[freq] -= 1
        sol[counts[freq]].append((string, freq))
    print(sol)
    for item in sol:
        for string, freq in item:
            yield string, str(-freq)


def count_sort(freqs: List[Tuple[str, int]]):
    print(freqs)
    maxval = min(map(lambda x: x[1], freqs))
    print(maxval)

    # build the counter and accumulate`
    counts = counter(freqs, maxval)
    counts = list(accumulate(counts))
    print(counts)

    yield from build_solution(freqs, counts)


def word_count_engine(document):
    valid = "abcdefghijklmnopqrstuvwxyz "

    # remove the punc
    document = [d for d in document if d.lower() in valid]
    # print(document)

    # standardise to lowercase
    document = [d.lower() for d in document]
    # print(document)

    # bring it together
    document = "".join(document)
    # print(document)

    document = document.split()
    # print(document)

    # create the counts of the word
    freqs = OrderedDict()
    for word in document:
        if word not in freqs:
            freqs[word] = 0
        freqs[word] += 1

    # sort them up
    freqs = list(freqs.items())
    freqs = [(s, -f) for s, f in freqs]

    ## one solution is by using the sorting using the normal sorting which is
    ## O(nlogn)
    #sol = [(s, -f) for s, f in sol]
    #sol = sorted(sol, key=lambda x: x[1])
    #return [[s, str(-f)] for s, f in sol]
    return [list(x) for x in count_sort(freqs)]



document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
print(word_count_engine(document))




"""
output: {word: freq}

no punc
case insensitive
sorted based on the freq


iterate and remove the punctuations: O(n)
at the same time make everything lowercase
split it based on the spaces

freq dict O(n)
sort it: O(nlogn)

"Practice makes perfect."
"practice makes perfect"
[practice, makes, perfect]
{pract..: 1, makes: 1, perfect: 1}


"""
