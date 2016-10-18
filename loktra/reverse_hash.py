from __future__ import print_function

def check_hash(giv_str):
    h = 7
    letters = "acdegilmnoprstuw"
    for i in giv_str:
        h = h * 37 + letters.index(i)
    return h

def reverse_hash(h):
    letters = "acdegilmnoprstuw"
    ind = []
    i = 0
    while h > 37:
        ind.append(int(h % 37))
        h /= 37

    broken_word = ""
    for i in reversed(ind):
        broken_word += letters[i]

    return broken_word


if __name__ == '__main__':
    print(check_hash(reverse_hash(930846109532517)) == 930846109532517)
