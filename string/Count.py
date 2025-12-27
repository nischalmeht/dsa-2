a = [
    ["D","D","D","G","D","D"],
    ["B","B","D","E","B","S"],
    ["B","S","K","E","B","K"],
    ["D","D","D","D","D","E"],
    ["D","D","D","D","D","E"],
    ["D","D","D","D","D","G"]
]

string = "GEEKS"
rows = len(a)
cols = len(a[0])
ans = 0

def solve(i, j, index):
    if index == len(string):
        return 1

    if i < 0 or j < 0 or i >= rows or j >= cols or a[i][j] != string[index]:
        return 0

    temp = a[i][j]
    a[i][j] = "0"  # mark visited

    found = (
        solve(i+1, j, index+1) +
        solve(i-1, j, index+1) +
        solve(i, j+1, index+1) +
        solve(i, j-1, index+1)
    )

    a[i][j] = temp  # backtrack
    return found

for i in range(rows):
    for j in range(cols):
        ans += solve(i, j, 0)

print(ans)
