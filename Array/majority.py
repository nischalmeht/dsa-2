nums = [2,2,1,1,1,2,2]
max_count=None
votes=0
for num in nums:
    if votes==0:
        max_count=num
        votes=1
    elif max_count==num:
        votes+=1
    else:
        votes-=1
print(max_count)