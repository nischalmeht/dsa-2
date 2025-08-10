intervals=[[1,3],[2,6],[8,10],[15,18]]
res=[]
current=intervals[0]
for i in range(1,len(intervals)):
    if current[1]<intervals[i][0]:
        res.append(current)
        current=intervals[i]
    else:
        current[1]=max(current[1],intervals[i][1])
res.append(current)

print(res)
    