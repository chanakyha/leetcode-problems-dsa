# leetcode link: https://leetcode.com/problems/set-matrix-zeroes/


def setMatrixZero(matrix):
    m = len(matrix)
    n = len(matrix[0])

    row, col = [0] *m, [0] * n

    for i in range(m):
        for j in range(n):
            if (matrix[i][j] == 0):
                row[i] = 1
                col[j] = 1
    
    for i in range(m):
        for j in range(n):
            if (row[i] == 1 or col[j] == 1):
                matrix[i][j] = 0

    return matrix


test_input = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
    ]

print(setMatrixZero(test_input))