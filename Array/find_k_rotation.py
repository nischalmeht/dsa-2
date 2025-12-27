# arr=[5, 6, 7, 4, 3, 2, 1]
# low=0
# high=len(arr)-1
# while low<=high:
#     mid=(low+high)//2
#     if arr[mid]>arr[high]:
#         low=mid+1
#     else:
#         high=mid-1
# print(low)


nums = [1,2,3,4,5,6,7]
k = 3
n=len(nums)
k%=n

def reverse(l,r):
    while l<r:
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
        r-=1
reverse(0,n-1)
reverse(0,k-1)
reverse(n,k-1)

print(nums)

