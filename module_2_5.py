def get_matrix(n, m, value):
    matrix = []
    if n <= 0 or m <= 0:
        return matrix
    for i in range(n):
        matrix.append([])
        for k in range(m):
            matrix[i].append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(4, 5, 45)
result3 = get_matrix(4, 2, 12)
print(result1)
print(result2)
print(result3)





