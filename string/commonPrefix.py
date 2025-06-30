strs = ["dog","racecar","car"]
s=sorted(strs)
first=s[0]
last=s[-1]
ans=""
for i in range(min(len(first),len(last))):
    if first[i]!=last[i]:
        print(ans)
        break
    ans+=first[i]
print(ans)