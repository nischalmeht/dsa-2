def print_subsequence(s,index=0,crrent=""):
    if index==len(s):
        print(crrent)
        return
    print_subsequence(s,index+1,crrent + s[index])
    print_subsequence(s , index+1,crrent)
str="abcd"
print_subsequence(str)