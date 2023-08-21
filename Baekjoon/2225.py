n, k = map(int, input().split())

mat = [[0 for _ in range(n+1)] for _ in range(k)]

for i in range(len(mat[0])):
    mat[0][i] = 1

for row in range(1, len(mat)):
    for col in range(len(mat[0])):
        mat[row][col] = mat[row-1][col] + mat[row][col-1]

print(mat[-1][-1]%1000000000)