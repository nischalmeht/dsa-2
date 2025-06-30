arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
i=0
j=len(arr)-1

while i<=j:
    if arr[i]<0:
        arr[i],arr[j]=arr[j],arr[i]
        j-=1
    else:
        i+=1
print(arr)