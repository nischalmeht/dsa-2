s1 = "aabcc"
s2 = "dbbca",
s3 = "aadbbcbcac"
def isInterleave(s1, s2, s3):
    if len(s1) + len(s2)!= len(s3):
        return False
    memo={}
    def solve(i,j,k):
        if k==len(s3):
            return True
        if (i,j) in memo:
            return memo[(i,j)]
        ans=False
        if i<len(s1) and s1[i]==s3[k]:
            if solve(i+1,j,k+1):
                ans=True
        if j<len(s2) and s2[j]==s3[k]:
            if solve(i,j+1,k+1):
                ans=True
        memo[(i,j)]=True
        return ans
    return solve(0,0,0)
print(isInterleave(s1,s2,s3))