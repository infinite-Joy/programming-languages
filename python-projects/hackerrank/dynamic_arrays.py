# https://www.hackerrank.com/challenges/dynamic-array/problem
# Class is created with values seq_list and last_answer and n with the number of sequences.
# We create two methods one for query 1 and the other for query 2.

# Helper methods:
#     Finding the sequence

# Query1:
#     Seq = (seq_list ^ last_answer) % N
#     Append integer y
# Query 2:
#     Seq = (seq_list ^ last_answer) % N
#     last _answer = y % size
#     Print last_answer

# ##########################

class SeqList:
    def __init__(self, n):
        self.n = n
        self.seq_list = [[] for _ in range(n)]
        self.last_answer = 0
        # print(self.n)
        # print(self.seq_list)

    def find_seq(self, x):
        index = (x ^ self.last_answer) % self.n
        # print('index', index)
        return index

    def query1(self, x, y):
        index = self.find_seq(x)
        self.seq_list[index].append(y)
        print(self.seq_list)

    def query2(self, x, y):
        index = self.find_seq(x)
        seq = self.seq_list[index]
        self.last_answer = seq[y % len(seq)]
        print(self.last_answer)

if __name__ == "__main__":
    n, q = [int(x) for x in input().split()]
    ins = SeqList(n)
    for _ in range(q):
        type_query, x, y = [int(x) for x in input().split()]
        if type_query == 1:
            ins.query1(x, y)
        elif type_query == 2:
            ins.query2(x, y)
        else:
            raise ValueError("other queries are not supported")
