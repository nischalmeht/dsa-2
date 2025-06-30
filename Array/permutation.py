arr = [1, 2, 3]
idx = -1
for i in range(len(arr) -2, -1, -1):  # i = 2, 1, 0
    if arr[i] < arr[i + 1]:           # arr[2+1] causes IndexError!
        idx = i
        break
if idx==-1:
    print(arr.reverse())
for i in range(len(arr)-1,-1,-1):
    if arr[i]>arr[idx]:
        arr[i],arr[idx]=arr[idx],arr[i]
        break
print(arr)