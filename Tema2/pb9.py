def seats(matrix):
    nrl = len(matrix)
    nrc = len(matrix[0])
    ret_list = []
    
    for col in range(nrc):
        for row in range(1, nrl):
            for prev_row in range(row):
                if matrix[row][col] <= matrix[prev_row][col]:
                    ret_list.append((row, col))
                    break
    
    return ret_list

print(seats([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]]))