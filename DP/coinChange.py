def coinChange(arr, amount):
    if amount < 1:
        return 0
    min_coins_dp = [float("inf")] * (amount + 1)
    min_coins_dp[0] = 0
    for i in range(1, amount + 1):
        for coin in arr:
            if coin <= i and min_coins_dp[i - coin] != float("inf"):
                min_coins_dp[i] = min(min_coins_dp[i], 1 + min_coins_dp[i - coin])
    return -1 if min_coins_dp[amount] == float("inf") else min_coins_dp[amount]
print(coinChange([1, 2, 5], 11))  
