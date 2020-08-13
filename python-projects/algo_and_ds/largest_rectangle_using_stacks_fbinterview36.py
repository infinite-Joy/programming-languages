# Complete the largestRectangle function below.
# to do this  you  need the stack approach
# reference https://www.youtube.com/watch?v=VNbkzsnllsU
# to do this we will need two stacks.
#

def evaluate_curr_stack(height_stack, position_stack, max_size, pos):
    temph = height_stack.pop()
    temp_pos = position_stack.pop()
    temp_size = temph * (pos-temp_pos)
    max_size = max(max_size, temp_size)
    return temp_pos, max_size



from math import inf

def largestRectangle(h):
    heights = h
    print(heights)

    height_stack = []
    position_stack = []

    max_size = -inf

    for pos, height in enumerate(heights):
        if len(height_stack) == 0 or height_stack[-1] < height:
            height_stack.append(height)
            position_stack.append(pos)
        elif height_stack[-1] > height:
            while height_stack and height < height_stack[-1]:
                temp_pos, max_size = evaluate_curr_stack(
                    height_stack, position_stack, max_size, pos)
            height_stack.append(height)
            position_stack.append(temp_pos)
        print(height_stack, position_stack, max_size)

    pos = pos + 1
    while height_stack:
        _, max_size = evaluate_curr_stack(
            height_stack, position_stack, max_size, pos)
        print(height_stack, position_stack, max_size)

    return max_size

print(largestRectangle([1,2,3,4,5]))
print(largestRectangle([3,2,3]))
