def dp(nums, start, end, k, p):
    print(start, end, k, p)
    if start > end or k <= 0:
        return 0
    if start == end:
        return int(k>=1)
    else:
        total = 0
            
        if nums[end] % p == 0 and nums[start] % p == 0:
            if k > 2:
                return dp(nums, start+1, end-1, k-2, p) + dp(nums, start, start, k-1, p) + dp(nums, end, end, k-1, p) + 1
            else:
                return dp(nums, start+1, end-1, k-2, p) + dp(nums, start, start, k-1, p) + dp(nums, end, end, k-1, p)
        elif nums[end] % p == 0 or nums[start] % p == 0:
            if nums[end] % p == 0:
                total += dp(nums, start, end-1, k-1, p) + dp(nums, start, end-1, k, p) + dp(nums, end, end, k-1, p)
            if nums[start] % p == 0:
                total += dp(nums, start+1, end, k-1, p) + dp(nums, start, end-1, k-1, p) + 3
        else:
            total += dp(nums, start+1, end-1, k, p) + 3

        print(total, 28)
            
        return total

nums = [2, 3, 3]
k = 2
p = 2
print(dp(nums, 0, len(nums)-1, k, p))