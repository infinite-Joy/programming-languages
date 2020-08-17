# Complete the poisonousPlants function below.
# i can implement stacks to find the final value of the remaining plants.
# then i can use the two pointer method to find the greatest difference between
# any two places in the stack.
# can be done in complexity O(n)
# space complexity O(n)

def poisonousPlants(p):
    #print(p)
    levels = p
    stack = []
    span = []
    for i, item in enumerate(levels):
        if not stack:
            span.append(0)
        else:
            span.append(i - stack[-1])
        if not stack or item < levels[stack[-1]]:
            stack.append(i)
        print(stack, span)
    if len(stack) == len(levels):
        return 0
    return max(span)

arr = [3,6,2,7,5]
print(poisonousPlants(arr))

arr = [6,5,8,4,7,10,9]
print(poisonousPlants(arr))

arr = [5,4,3,2,1]
print(poisonousPlants(arr))

arr = [1,2,3,4,5]
print(poisonousPlants(arr))
