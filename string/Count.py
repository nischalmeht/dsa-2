a = [
    ["D","D","D","G","D","D"],
    ["B","B","D","E","B","S"],
    ["B","S","K","E","B","K"],
    ["D","D","D","D","D","E"],
    ["D","D","D","D","D","E"],
    ["D","D","D","D","D","G"]
]
string = "GEEKS"
rows=len(a)
ans=0
column=len(a[0])
def solve(i,j,string,a,rows,column,index):
    found=0
    if i>=0 and j>=0 and i<rows and j<column and string[index]==a[i][j]:
        temp=a[i][j]
        a[i][j]="0"
        index+=1
        if index==len(string):
            found=1
        else:
            found+=solve(i+1,j,string,a,rows,column,index)
            found+=solve(i-1,j,string,a,rows,column,index)
            found+=solve(i,j+1,string,a,rows,column,index)
            found+=solve(i,j-1,string,a,rows,column,index)
        a[i][j]=temp
    return found
print(ans)
for i in range(rows):
    for j in range(column):
        ans+=solve(i,j,string,a,rows,column,0)


