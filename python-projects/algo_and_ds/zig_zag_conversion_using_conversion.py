"""
for this can use a list of queues

[pa,apl,yi]

time: O(n)
space: O(n)

"""



class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 1 or numRows == 1:
            return s
        # print(s)
        rows = [[] for _ in range(numRows)]
        i = 0
        movement = -1
        for ch in s:
            # print(ch, i)
            if i == 0 or i == (numRows - 1):
                movement *= -1
            rows[i].append(ch)
            # print(rows)
            i += movement
        pattern = [ch for sublist in rows for ch in sublist]
        return "".join(pattern)