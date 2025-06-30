arr=  [9, 8, 7, 6, 4, 2, 1, 3]
k=1
def revers(arr,l,r):
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1

n=len(arr)
k=k%n
revers(arr,0,n-1)
revers(arr,0,k-1)
revers(arr,k,n-1)
print(arr)