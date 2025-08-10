def coinChange(coins,amount):
    if amount<1:
        return 1
    coins_dp=[float("inf")] * (1+amount)
    coins_dp[0]=0
    for i in range(1,1+amount):        
        for coin in coins:
            if coin <=i and coins_dp[i-coin]!=float("inf"):
                coins_dp[i]=min(coins_dp[i],1+ coins_dp[i-coin])
    return -1 if coins_dp[amount]==float("inf") else coins_dp[amount]

print(coinChange([1,2,5],11))        