from collections import defaultdict

def print_matrix(mat, first_row, first_col, last_row, last_col, visited):
    # stopping condition
    #if len(visited) >= len(mat) * len(mat[0]):
    #    return
    if first_row > last_col or first_col > last_col:
        return

    # right -> left
    for j in range(first_col, last_col+1):
        #visited[(first_row, j)] = True
        print(mat[first_row][j])
    first_row += 1

    # top -> down
    for j in range(first_row, last_row+1):
        #visited[(j, last_col)] = True
        print(mat[j][last_col])
    last_col -= 1

    # right -> left
    for j in range(last_col, first_col-1, -1):
        #visited[(last_row, j)] = True
        #print(visited)
        print(mat[last_row][j])
    last_row -= 1

    # bottom -> top
    for j in range(last_row, first_row-1, -1):
        #visited[(j, first_col)] = True
        print(mat[j][first_col])
    first_col += 1

    # go to the inner mat
    print_matrix(mat, first_row, first_col, last_row, last_col, visited)


mat = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
]

visited = defaultdict(bool)
print_matrix(mat, 0, 0, len(mat)-1, len(mat[0])-1, visited)
