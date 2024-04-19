# Q14. Write a Python Program to Add Two Matrices. 

matrix1 = [[2,4,5], [3,9,1], [5,3,1]]
matrix2 = [[6,6,4], [3,9,1], [11,0,0]]

# matrices must be of same order

matrixResult = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        matrixResult[i][j] = matrix1[i][j] + matrix2[i][j]


print(matrixResult)
