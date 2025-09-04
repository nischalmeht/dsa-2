def partition(arr):
    total = sum(arr)
    if total % 2 != 0:
        return False
    target = total // 2
    memo = {}

    def recursion(index, current):
        key = f"{index}-{current}"
        if key in memo:
            return memo[key]
        if current < 0:
            return False
        if current == 0:
            return True
        if index == len(arr):
            return False

        memo[key] = (
            recursion(index + 1, current - arr[index]) or 
            recursion(index + 1, current)
        )
        return memo[key]

    return recursion(0, target)


print(partition([1, 5, 11, 5]))  # ✅ Expected: True
