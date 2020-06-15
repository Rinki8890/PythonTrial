import numpy as np
mat = [[100, -350, -200],
        [-100, -300, 700]]

visited = []
#(i+1, j), or, (i, j+1), or (i+1, j+1)
sum_ = mat[0][0]
for i in range (1):
    for j in range (2):
        if (mat[i+1][j]>mat[i][j+1] and mat[i+1][j]>mat[i+1][j+1]):
            sum_ +=mat[i+1][j]
            print("1..",sum_)
            sum_+=mat[i][j+1]
            visited.append(mat[i][j+1])
        elif (mat[i][j+1]>mat[i+1][j] and mat[i][j+1] >mat[i+1][j+1]):
            sum_ +=mat[i+1][j+1]
            print("2..",sum_)
        elif (mat[i+1][j+1]>mat[i][j+1] and mat[i+1][j+1]>mat[i+1][j]):
            sum_ +=mat[i+1][j+1]
            print("3..",sum_)
        else:
            sum_ +=0
print(sum_)
            
    