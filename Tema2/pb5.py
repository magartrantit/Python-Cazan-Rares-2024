def matrix_replace(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i ==j:
                m[i][j] = 0
    return m

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_replace(m))