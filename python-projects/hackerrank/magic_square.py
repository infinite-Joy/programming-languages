import math

def check_magic_sq(sq):
    possible_count = sum(sq[:3])
    rows = [[sq[i] for i in range(3*st, 3*st+3)] for st in range(0, 3)]
    for row in rows:
        if possible_count != sum(row):
            return False
    cols = [[sq[i], sq[i+3], sq[i+6]] for i in range(3)]
    for col in cols:
        if possible_count != sum(col):
            return False
    diags = [[sq[0], sq[4], sq[8]], [sq[2], sq[4], sq[6]]]
    for d in diags:
        if possible_count != sum(d):
            return False
    return True


def magic_squares(sofar, rest, answer):
    #print(sofar, rest, answer)
    if answer is None:
        answer = []
    if sofar is None:
        sofar = []
    if rest == []:
        if check_magic_sq(sofar):
            answer.append(sofar)
    else:
        for i, ch in enumerate(rest):
            next_ch = sofar + [ch]
            remaining = rest[:i] + rest[i+1:]
            magic_squares(next_ch, remaining, answer)
        return answer

sqs = magic_squares(None, [1,2,3,4,5,6,7,8,9], None)
print(sqs)
print(len(sqs))
#print(check_magic_sq([2,7,6,9,5,1,4,3,8]))
#print(check_magic_sq([1,2,3,4,5,6,7,8,9]))

def cost(msq, mysq):
    c = [math.fabs(i-j) for i,j in zip(msq, mysq)]
    print(c)
    return sum(c)


def formingMagicSquare(s):
    sq = []
    for elems in s:
        for i in elems:
            sq.append(i)

    print('sq', sq)
    sqs = magic_squares(None, [1,2,3,4,5,6,7,8,9], None)
    print("all magic sqs", sqs)
    curr_min = 10000000
    for msq in sqs:
        print(msq)
        curr_min = min(curr_min, cost(msq, sq))
    return curr_min

print(formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]]))
print
