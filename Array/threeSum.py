arr = [1, 4, 45, 6, 10, 8] 
target = 13 
result = []

arr.sort()  # Correct sorting
print("Sorted array:", arr)

for i in range(0, len(arr) - 2):
    left = i + 1
    right = len(arr) - 1

    while left < right:
        sum_val = arr[i] + arr[left] + arr[right]
        if sum_val == target:
            result.append((arr[i], arr[left], arr[right]))
            left += 1
            right -= 1
        elif sum_val < target:
            left += 1
        else:
            right -= 1

print("Triplets with target sum:", result)
