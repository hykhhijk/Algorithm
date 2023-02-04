import sys 

n = int(input())
mat = [[] for _ in range(n)]
for i in range(n):
    mat[i]=list(map(int, sys.stdin.readline().split()))

for i in range(n):
    for j in range(n):
        if mat[i][j]==0:
            mat[i][j]=101
for k in range(n):
    for i in range(n):
        for j in range(n):
            mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])

for i in range(n):
    for j in range(n):
        if mat[i][j]==101:
            print("0 ", end="")
        else:
            print("1 ", end="")
    print()