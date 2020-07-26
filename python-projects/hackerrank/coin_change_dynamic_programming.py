def coins_change(coins, amount):
    dp = [amount+1] * (amount+1)
    dp[0] = 0

    for i in range(1, amount+1):
        print(dp)
        for c in coins:
            if i >= c:
                dp[i] = min(dp[i], dp[i-c]+1)
    print(dp)

    if dp[amount] == amount+1:
        return -1
    return dp[amount]

#coins = [1, 2, 5]
#print(coins_change(coins, 11))

coins = [2,5]
print(coins_change(coins, 11))

