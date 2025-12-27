nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

max_one=0
zerocount=0
start=0
for right in range(len(nums)):
    if nums[right]==0:
        zerocount+=1
    while zerocount>k:
        if nums[start]==0:
            zerocount-=1
        start+=1
    max_one=max(max_one,right-start+1)
print(max_one)

