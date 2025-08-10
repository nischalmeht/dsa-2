def row_with_max_ones(matrix):
    n = len(matrix)
    m = len(matrix[0])
    max_row_index = -1
    j = m - 1  
    for i in range(n):
        while j >= 0 and matrix[i][j] == 1:
            max_row_index = i
            j -= 1
    return max_row_index

matrix = [
    [0, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]
print("Row with max 1s:", row_with_max_ones(matrix))
