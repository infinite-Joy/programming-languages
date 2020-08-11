"""
Finding the subset problem using the knapsack algorithm and dynamic programmings

time complexity: O(mn)
space complexity: O(mn)


"""

from pprint import pprint

def is_subset_sum(nums, total):
    # create the tabulation table and set them to False
    table = [[False for _ in range(total+1)] for _ in range(len(nums)+1)]

    # set the first col to true as we can select nothing with nothing
    table[0][0] = True
    for i, _ in enumerate(nums):
        table[i+1][0] = True

    for i, item in enumerate(nums, 1):
        for j in range(1, total+1):
            if j < item:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i-1][j] or table[i-1][j-item]

    pprint(table)
    if table[-1][-1] is True:
        return table


def get_selections(table, nums):
    i = len(table) - 1
    j = len(table[0]) - 1
    selections = []
    while j > 0: # as soon as we reach the first col we are done
        print(i, j, selections)
        #__import__('pdb').set_trace()
        if table[i][j] is True and table[i-1][j] is True:
            pass # this is not selected
        elif table[i][j] is True and table[i-1][j] is False:
            selections.append(i)
            j = j - nums[i-1]
        else:
            raise ValueError('this sholud not happen')
        i -= 1
    return [nums[x] for x in selections[:-1]]



nums = [3, 34, 4, 12, 5, 2]
nums = sorted(nums)
print(nums)
table = is_subset_sum(nums, 9)
print(get_selections(table, nums))


