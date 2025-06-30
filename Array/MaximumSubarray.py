arr=[-1, -3, -10, 0, 6]
left_subarray=1
right_subarray=1
result=arr[0]
for i in range(0,len(arr)):
    left_subarray = 1 if left_subarray == 0 else left_subarray
    right_subarray = 1 if right_subarray == 0 else right_subarray
    
    left_subarray*=arr[i]
    right_subarray*=arr[len(arr)-1-i]

    result=max(left_subarray,right_subarray,result)
print(result)

    