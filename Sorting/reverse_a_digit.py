def reverse_number(n):
    reversed_num = 0
    negative = n < 0
    n = abs(n)

    while n > 0:
        digit = n % 10          
        reversed_num = reversed_num * 10 + digit
        n = n // 10           

    return -reversed_num if negative else reversed_num

# Example
print(reverse_number(1234))   # Output: 4321
print(reverse_number(-5678))  # Output: -8765
