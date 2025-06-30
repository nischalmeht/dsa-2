arr = [7,1,5,3,6,4]
min_price=arr[0]
max_profit=0
for i in range(0,len(arr)):
    min_price=min(min_price,arr[i])
    profit=arr[i]-min_price
    max_profit=max(profit,max_profit)
print(max_profit)
