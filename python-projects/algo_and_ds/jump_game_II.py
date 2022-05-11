"""
trying to model this along the lines of the jump game 1

"""


def jump_game_2(nums):
    print(nums)
    dis = 0
    i = 0
    limit = len(nums) - 1
    jumps = 0
    while i < limit:
        dis = min(i + nums[i], limit)
        print(f'{i=}, {dis=}')
        nextpos = (nums[i], i)
        for j in range(i+1, dis+1):
            nextpos = max(nextpos, (nums[j], j))
        i = nextpos[1]
        if dis < limit:
            jumps += 1
        else:
            i = limit
    return jumps


def jump_game_2(nums):
    left = right = 0
    limit = len(nums) - 1
    jumps = 0
    while right < limit:
        farthest = 0
        for i in range(left, right+1):
            farthest = max(farthest, i + nums[i])
        left = right + 1
        right = farthest
        jumps += 1
    return jumps



nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
print(jump_game_2(nums), 'actual', 2)