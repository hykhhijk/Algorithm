import sys

n = int(input())
mine_mat = []
for _ in range(n):
    mine_mat.append(list(sys.stdin.readline().strip()))
mat = []
for _ in range(n):
    mat.append(list(sys.stdin.readline().strip()))

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]
check = False
result_mat = [["."]*n for _ in range(n)]
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j]=="x":
            count = 0
            if mine_mat[i][j]=="*":
                check = True
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if x < 0 or x >=n or y < 0 or y >=n:
                    continue
                if mine_mat[x][y]=="*":
                    count+=1
            result_mat[i][j] = count
if check==True:
    for i in range(len(mine_mat)):
        for j in range(len(mine_mat[i])):
            if mine_mat[i][j]=="*":
                result_mat[i][j] = "*"

for i in result_mat:
    print("".join(map(str, i)))