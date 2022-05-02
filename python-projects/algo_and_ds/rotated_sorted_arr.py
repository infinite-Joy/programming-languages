def get_greatest(nums):
    low = 0
    hi = len(nums) - 1
    if nums[low] <= nums[hi]:
        return hi
    while low <= hi:
        if low == hi:
            return low

        mid = int((low + hi) / 2) # 7
        if nums[mid] > nums[hi]: # 0 and 2
            low = mid # 7 - 2
        else:
            hi = mid - 1 # this targets 7
            
def normal_bin_search(nums, i, j, target): # this is fine because each part is sorted by itself.
    low = i
    hi = j
    while low <= hi:
        if low == hi:
            return low

        mid = int((low + hi) / 2)
        if nums[mid] < target:
            low = mid + 1
        else:
            hi = mid

nums = [1, 3]
target = 0
    
lval = get_greatest(nums) # get the greatest
print(lval)
if target >= nums[0]: # this means that this is on the left side of the arr
    possible = normal_bin_search(nums, 0, lval, target) # 0, 7
else:
    possible = normal_bin_search(nums, lval+1, len(nums)-1, target)
print('possible', possible)
# if possible is not None and nums[possible] == target:
#     return possible