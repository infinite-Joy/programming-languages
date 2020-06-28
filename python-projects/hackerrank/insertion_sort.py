# this is not to be implemented in code
# just for learning reasons
# insertion sort is On

x = [5,2,4,6,1,3]
for i in range(1, len(x)):
    curr_ind = i
    while curr_ind > 0 and x[curr_ind] < x[curr_ind-1]:
        x[curr_ind], x[curr_ind-1] = x[curr_ind-1], x[curr_ind]
        curr_ind -= 1
        print(i, curr_ind, x)
        print("#"*10)
