import math
piles = [3,6,7,11]
h = 8
left=1
right=max(piles)
while left<=right:
    mid=(left+right)//2
    hr=0
    for pile in piles:
        hr+=math.ceil(pile/mid)
    if hr<=h:
        right=mid-1
    else:
        left=mid+1
print(left)

    