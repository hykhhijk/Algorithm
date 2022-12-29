import sys

n, m = map(int, input().split())
mat = []
targets=[]
for _ in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))
for _ in range(m):
    targets.append(list(map(int, sys.stdin.readline().split())))
for i in range(len(targets)):
    for j in range(len(targets[i])):
            targets[i][j] -= 1
dp_mat = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i==0 and j==0:
            dp_mat[i][j] = mat[i][j]
        elif i==0:
            dp_mat[i][j] = mat[i][j] + dp_mat[i][j-1]
        elif j==0:
            dp_mat[i][j] = mat[i][j] + dp_mat[i-1][j]
        else:
            dp_mat[i][j] = dp_mat[i-1][j] + dp_mat[i][j-1] - dp_mat[i-1][j-1] + mat[i][j]

for i in range(len(targets)):
    row1, col1, row2, col2 = targets[i]
    if row1==0 and col1==0:
        result = dp_mat[row2][col2] 
    elif row1==0:
        result = dp_mat[row2][col2] - dp_mat[row2][col1-1]
    elif col1==0:
        result = dp_mat[row2][col2] - dp_mat[row1-1][col2]
    else:
        result = dp_mat[row2][col2] - dp_mat[row1-1][col2] - dp_mat[row2][col1-1] + dp_mat[row1-1][col1-1]
    
    print(result)