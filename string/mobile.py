mapping = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
digit="23"
result=[]
def recursion(index,current=""):
    if index==len(digit):
        result.append(current)
        return
    for letter in mapping[digit[index]]:
        recursion(index+1,current+letter)
recursion(0,"")
print(result)

    