prices = [10, 22, 5, 75, 65, 80]
profit=0
for i in range(1,len(prices)):
    if prices[i]>prices[i-1]:
        profit+=(prices[i]-prices[i-1])
print(profit)        