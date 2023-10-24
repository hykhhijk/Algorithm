n, k = map(int, input().split())

mat = [[0 for _ in range(n+1)] for _ in range(k)]

for i in range(len(mat[0])):
    mat[0][i]=1

for i in range(1, len(mat)):
    for j in range(len(mat[0])):
        mat[i][j] = mat[i-1][j] + mat[i][j-1]

print(mat[-1][-1]%1000000000)