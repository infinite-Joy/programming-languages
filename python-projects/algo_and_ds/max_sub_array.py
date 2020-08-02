"""
Using dynamic prpgramming

Kadane algo https://www.youtube.com/watch?time_continue=596&v=86CQq3pKSUw&feature=emb_logo

complexity: O(n)
"""
def max_sub_array(nums):
    current_sum = nums[0]
    total_sum = nums[0]

    for item in nums:
        # Current max sum is either the current element OR current element +
        # Previous Maximum subarray)
        current_sum = max(current_sum + item, item)

        # if current sum is greater than the global total then update it
        total_sum = max(current_sum, total_sum)

    return total_sum

print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
