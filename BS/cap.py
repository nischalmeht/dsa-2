weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
right = sum(weights)
left = max(weights)

def can_ship(capacity):
    day = 1
    cl = 0
    for w in weights:
        if cl + w > capacity:
            day += 1
            cl = 0
        cl += w
    return day <= days

while left <= right:
    mid = (left + right) // 2
    if can_ship(mid):
        right = mid - 1 
    else:
        left = mid + 1  

print(left)  
