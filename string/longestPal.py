# O(n^2) time, O(n) recursion depth
def longest_palindrome_recursive(s):
    if not s or len(s) == 1:
        return s

    def expand(l: int, r: int) -> str:
        if l < 0 or r >= len(s) or s[l] != s[r]:
            return s[l+1:r]
        return expand(l-1, r+1)

    best = s[0]

    for i in range(len(s)):
        odd = expand(i, i)
        if len(odd) > len(best):
            best = odd

        even = expand(i, i+1)
        if len(even) > len(best):
            best = even

    return best

# Examples
print(longest_palindrome_recursive("babad"))  # "bab" or "aba"
print(longest_palindrome_recursive("cbbd"))   # "bb"
print(longest_palindrome_recursive("a"))      # "a"
