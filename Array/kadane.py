arr= [-2, -4]
current_sum=0
max_sum=float("-inf")
i=0
for i in range(len(arr)):
    current_sum+=arr[i]
    max_sum=max(current_sum,max_sum)
    if current_sum<0:
        current_sum=0
i+=1
print(max_sum)
