
def find(nums):
    total = 0
    for i, elem in enumerate(nums):
        print(total, i, elem)
        total ^= i ^ elem
    return total

nums = [1,3,4,2,2]
# print(find(nums))

sortedn = sorted(nums)
print(find(sortedn))


"""
can do the xor thing here.

the xor thing will not work here as there can be multiple duplicates

sort and do a bisect left and bisect right
or to create a map. lets see how different they are

==========================

nums = [1,  3,  4,  2,  2]
                    _
                        _

"""




class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mapping = {}
        for el in nums:
            if el not in mapping:
                mapping[el] = True
            else:
                return el
        
#         slow, fast = nums[0], nums[nums[0]]
#         while slow != fast:
#             slow, fast = nums[slow], nums[nums[fast]]
            
#         slow = nums[0]
#         while slow != fast:
#             slow, fast = nums[slow], nums[fast]
#         return slow
        
