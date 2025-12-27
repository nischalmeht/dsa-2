arr = [2, 3, 4, 7, 11]
k = 5

left = 0
right = len(arr) - 1
print(right)
while left <= right:
    mid = (left + right) // 2
    missing = arr[mid] - (mid + 1) 
    if missing < k:
        left = mid + 1
    else:
        right = mid - 1

print(k + left)  
